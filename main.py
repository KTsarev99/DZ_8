import data_generation as dg
import view as ui
import logger
import crud


# dg.start() # генерация базы контактов
logger.logging.info('Start')
crud.init_data_base('base_phone.csv')
ui.ls_menu()