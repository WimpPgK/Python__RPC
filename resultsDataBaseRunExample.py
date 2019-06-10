
from ResultsDataBase import ResultsDataBase

if __name__ == '__main__':
    resultsDataBase = ResultsDataBase()
    result = ('test program', '54.456')
    result_id = resultsDataBase.add_program_result(result)

    print("All results from base:")
    resultsDataBase.select_all_results()
