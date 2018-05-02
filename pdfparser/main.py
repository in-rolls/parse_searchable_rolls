from modules.args import get_args
from modules.parse import RollParser
from modules.logger import log_configurer, LogFacility


def main():
    args = get_args()
    log_configurer()
    logger = LogFacility()
    logger.banner()
    try:
        RollParser(path=args.path, state=args.state, lang=args.lang, output=args.out, resume=args.resume)
    except KeyboardInterrupt:
        pass
    except Exception as exc:
        logger.error(exc)
    finally:
        logger.info('Exited.')


if __name__ == '__main__':
    main()
