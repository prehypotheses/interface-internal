"""Module cli.py"""
import logging
import os

import transformers

import config


class CLI:
    """
    Command Line Interface
    """

    def __init__(self, arguments: dict):
        """

        :param arguments: A set of arguments vis-à-vis calculation, interface, and storage objectives.
        """

        self.__configurations = config.Config()

        # Pipeline
        # noinspection PyTypeChecker
        self.__classifier = transformers.pipeline(
            task='ner', model=os.path.join(self.__configurations.data_, 'model'),
            device=arguments.get('device'))

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)30d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def exc(self, ):
        """

        :return:
        """

        # Sample Text
        text = input('Please input text (Maximum: 2000 Characters): ')

        # Re-print the input
        self.__logger.info('Text: %s', text)

        # Hence
        self.__logger.info(self.__classifier(text))
