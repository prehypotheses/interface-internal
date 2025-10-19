"""Module main.py"""
import argparse
import logging
import os
import sys

import boto3


def main():
    """
    Entry Point

    :return:
    """

    logger: logging.Logger = logging.getLogger(__name__)

    logger.info('Re-acquire: %s', arguments.get('reacquire'))
    if arguments.get('reacquire'):
        src.data.interface.Interface(s3_parameters=s3_parameters).exc()

    # Explore/Interact
    src.clients.interface.Interface(
        service=service, s3_parameters=s3_parameters, arguments=arguments).exc(client='future')

    # Delete Cache Points
    src.functions.cache.Cache().exc()


if __name__ == '__main__':

    # Paths
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Activate graphics processing units
    os.environ['CUDA_VISIBLE_DEVICES']='0'
    os.environ['TOKENIZERS_PARALLELISM']='true'
    os.environ['HF_HOME']='/tmp'

    # Classes
    import src.clients.interface
    import src.data.interface
    import src.elements.s3_parameters as s3p
    import src.elements.service as sr
    import src.functions.cache
    import src.preface.interface
    import src.variables


    # The arguments, i.e., input variables.
    variables = src.variables.Variables()
    parser = argparse.ArgumentParser()
    parser.add_argument('--reacquire', type=variables.reacquire,
                        help=('Either True or False.  In answer to the question - '
                              'Should the model artefacts be reacquired?'))
    args = parser.parse_args()

    connector: boto3.session.Session
    s3_parameters: s3p
    service: sr.Service
    arguments: dict
    connector, s3_parameters, service, arguments = src.preface.interface.Interface().exc(reacquire=args.reacquire)

    main()
