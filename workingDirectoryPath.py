import os
import logging

#class changeDirectory:

def __init__():
    v_initial_directory=os.getcwd()
    return v_initial_directory

def initialization_logs(v_initial_directory):

    try:
        v_current_directory=os.path.dirname(os.path.abspath(__file__))
    except:
        print('Impossible to change the directory to put the log file with the python file, look at ChangeDirectory.f_new_directory')
        
    # Créer le logger
    logger = logging.getLogger('mon_application')
    logger.setLevel(logging.DEBUG)  # Capture tous les logs de niveau DEBUG et au-dessus

    # Créer le handler pour les logs INFO
    handler_info = logging.FileHandler(f'{v_current_directory}\logs_info.log')
    handler_info.setLevel(logging.INFO)
    formatter_info = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(message)s')
    handler_info.setFormatter(formatter_info)
    logger.addHandler(handler_info)

    # Créer le handler pour les logs ERROR
    handler_error = logging.FileHandler(f'{v_current_directory}\logs_error.log')
    handler_error.setLevel(logging.ERROR)
    formatter_error = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(message)s')
    handler_error.setFormatter(formatter_error)
    logger.addHandler(handler_error)

    # Exemples d'utilisation
    logger.info("Log info initialization.")
    logger.error("Log error initialization")
    logger.info(f'initial directory : {v_initial_directory}')

    return v_current_directory

def f_change_directory(v_current_directory):

    try:
        os.chdir(v_current_directory)
    except:
        logging.error(f'Error impossible to change working directory for py file directory')

v_initial_directory=__init__()
v_current_directory=initialization_logs(v_initial_directory)
f_change_directory(v_current_directory)