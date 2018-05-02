import re
from collections import deque, Counter
from operator import itemgetter
from ..base import Reader, Patterns, Elector

__all__ = ['AndhraPDF']


class AndhraPatterns(Patterns):
    box_patterns = dict(
        main=r'(\d+\nElector\'s(.*?(?=\d+\nElector)|.*))',
        addition=r'(Age:(.*?(?=Age:)|.*))',
        correction=r'(\d+\sAge:(.*?(?=\d+\sAge:)|.*))',
    )

    general_patterns = dict(
        state=r'(?<=State - )[^\n]+',
        acName=r'(?<=\n)(\d+ [a-zA-Z ()]+)(?=\n)',
        pcName=r'District\n:\n(.*?)(?=\n\d+\n)',
        acStatus=r'(?<=Part No.\n)([A-Z]+)(?=\n)',
        partNo=r'(?<=\n)(\d+)(?=\n\d+ [a-zA-Z ()]+\n)',
        year=r'(?<=\n)(20\d{2})',
        mainTown=r'Third Gender\n\d+\n([^\n]+)',
        policeStation=r'(?<=\n\d{6}\n)([^\n]+)',
        mandal=r'([^\n]+)(?=\n\d{6}\n)',
        revenueDivision=r'([^\n]+)(?=\n[^\n]+\n\d{6}\n)',
        district=r'Third Gender\n\d+\n[^\n]+\n([^\n]+)',
        stationName=r'(?<=\n)([A-Z\s]+)(?=[0-9\n]+Third Gender\n)',
        stationAddress=r'(?<=Total\nFemale\nMale\n)([^a-z]+?)(?=\n[^a-z\n]+\n\d+)',
        netMale=r'(?<=\n)(\d+)(?=\n\d+\n\d+\nThird Gender\n)',
        netFemale=r'(?<=\n)(\d+)(?=\n\d+\nThird Gender\n)',
        netThird=r'(?<=Third Gender\n)(\d+)(?=\n)',
        netTotal=r'(?<=\n)(\d+)(?=\nThird Gender\n)'
    )

    elector_patterns = dict(
        number=r'(\d+)\n(?=Elector\'s Name:|Age:)',
        name=r'(?<=\n)([A-Z\s.-]{5,})(?=\n)',
        house=r'((D.N0 )?\d+[-/]\d+([-/][0-9a-zA-Z]+)*)',
        age=r'(?<=\n)(\d+)\n(?=Male|Female|Third Gender|\d+\nElector|[A-Z ]{3,})',
        sex=r'(?<=[ \n])(Male|Female|Third Gender)(?=\n[A-Z ]{3,}|\n)',
    )


class AndhraElector(Elector):
    reverses = {'addition', 'correction'}
    skiptxts = [re.compile(r'(D\s*E\s*L\s*E\s*T\s*E\s*D)')]

    def __init__(self, *args, **kwargs):
        super(AndhraElector, self).__init__(*args, **kwargs)

    def parse(self):
        def last(w):
            try:
                return w[-1].lower().strip()
            except IndexError:
                return ''

        def skip(w):
            return [i for i in w if len(i) > 1]

        def rule_lname(skip_=False):
            lw = skip(l_words) if skip_ else l_words
            rw = skip(r_words) if skip_ else r_words
            if last(o_words) == last(rw):
                left.append(odd)
                return True
            elif last(lw) == last(rw):
                right.insert(0, odd)
                return True
            else:
                return False

        def rule_1_1(skip_=False):
            lw = skip(l_words) if skip_ else l_words
            rw = skip(r_words) if skip_ else r_words
            if len(lw) == len(rw) == 1:
                if self.reversed:
                    right.insert(0, odd)
                else:
                    left.append(odd)
                return True
            return False

        def rule_2_1(skip_=False):
            lw = skip(l_words) if skip_ else l_words
            rw = skip(r_words) if skip_ else r_words
            if len(lw) == 2 and len(rw) == 1:
                right.insert(0, odd)
                return True
            elif len(lw) == 1 and len(rw) == 2:
                left.append(odd)
                return True
            else:
                return False

        def rule_2_2(skip_=False):
            lw = skip(l_words) if skip_ else l_words
            rw = skip(r_words) if skip_ else r_words
            if len(lw) == len(rw) == 2:
                if self.reversed:
                    right.insert(0, odd)
                else:
                    left.append(odd)
                return True
            return False

        def rule_less_win(skip_=False):
            lw = skip(l_words) if skip_ else l_words
            rw = skip(r_words) if skip_ else r_words
            if len(lw) < len(rw):
                left.append(odd)
                return True
            elif len(rw) < len(lw):
                right.insert(0, odd)
                return True
            else:
                return False

        def rule_ele_win():
            if self.reversed:
                right.insert(0, odd)
            else:
                left.append(odd)
            return True

        def parts_to_words():
            ret = []
            for i in parts:
                ret.extend(i.split())
            return ret

        def refine_words(n=1, oddcase=False):
            refined = [(i, w) for i, w in enumerate(words) if len(w) > n]
            skips = [(i, w) for i, w in enumerate(words) if len(w) <= n]
            s = len(refined) // 2
            if len(refined) % 2 == 0:
                lt = refined[:s]  # list of left refined words with indexes
                rt = refined[s:]  # list of right refined words with indexes
                middle = lt[-1][0]  # position of separation
                for i in skips:
                    if i[0] > middle:
                        rt.append(i)
                    else:
                        lt.append(i)
                left.extend([i[1] for i in sorted(lt, key=itemgetter(0))])
                right.extend([i[1] for i in sorted(rt, key=itemgetter(0))])
                return True
            if oddcase:
                s += 1
                lt = refined[:s]
                rt = refined[s:]
                middle = lt[-1][0]
                for i in skips:
                    if i[0] > middle:
                        rt.append(i)
                    else:
                        lt.append(i)
                left.extend([i[1] for i in sorted(lt, key=itemgetter(0))])
                right.extend([i[1] for i in sorted(rt, key=itemgetter(0))])
                return True
            return False

        names = self.find('name', alter=False)
        parts = names.split('\n')
        count = len(parts)
        left = deque()
        right = deque()
        if count == 1:
            if self.reversed:
                right.insert(0, parts[0])
            else:
                left.append(parts[0])
        elif count % 2 == 0:
            stop = count // 2
            left.extend(parts[:stop])
            right.extend(parts[stop:])
        elif count == 3:
            if len(parts[-1]) == 1 and len(parts[1]) > 1:
                left.append(parts[0])
                right.append('%s%s' % (parts[1], parts[-1]))
            else:
                left.append(parts[0])
                right.append(parts[-1])
                odd = parts[1]
                l_words = left[-1].split()
                r_words = right[-1].split()
                o_words = odd.split()
                _ = rule_lname() or \
                    rule_1_1() or \
                    rule_2_1() or \
                    rule_2_2() or \
                    rule_lname(True) or \
                    rule_1_1(True) or \
                    rule_2_1(True) or \
                    rule_2_2(True) or \
                    rule_less_win(True) or \
                    rule_ele_win()
        elif count > 4:
            words = parts_to_words()
            counter = Counter(parts)
            common = counter.most_common(1)
            common_word = common[0][0]
            common_count = common[0][1]
            if common_count == 2:
                if words[-1] == common_word:
                    stop = words.index(common_word) + 1
                    left.extend(words[:stop])
                    right.extend(words[stop:])
                elif words[0] == common_word:
                    stop = words[1:].index(common_word) + 1
                    left.extend(words[:stop])
                    right.extend(words[stop:])
            else:
                if not refine_words(n=1) and not refine_words(n=2) and not refine_words(n=2, oddcase=True):
                    raise NotImplementedError('Unable to parse elector\'s name: %s' % parts)
        else:
            raise NotImplementedError('Unable to parse elector\'s name: %s' % parts)

        # Store parsed result
        if self.reversed:
            self.name = ' '.join(right).strip()
            self.relative_name = ' '.join(left).strip()
        else:
            self.name = ' '.join(left).strip()
            self.relative_name = ' '.join(right).strip()


class AndhraPDF(Reader):
    pat = AndhraPatterns()

    def __init__(self, path):
        super(AndhraPDF, self).__init__(path, cls_elector=AndhraElector)
