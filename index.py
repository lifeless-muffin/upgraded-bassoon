# load environment varaibles
from dotenv import load_dotenv
load_dotenv() # configuration

# import servies and modules
from services.database.database import DatabaseManager, search_documents
import services.language.language as language
import services.engine.engine as engine

def main():

    # call the engine
    engine.__init__()


if __name__ == '__main__':
    main()