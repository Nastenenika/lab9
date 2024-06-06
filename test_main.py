from data.csv import work
def test_work_1():
    lines = [
        '6,0,3,"Moran, Mr. James",male,,0,0,330877,8.4583,,Q',
             '7,0,1,"McCarthy, Mr. Timothy J",male,54,0,0,17463,51.8625,E46,S',
             '8,0,3,"Palsson, Master. Gosta Leonard",male,2,3,1,349909,21.075,,S'
        ]

    assert work(lines) == (0, 0, 7, 0)

def test_work_2():
    lines = [
        '6,1,3,"Moran, Mr. James",male,,0,1,330877,8.4583,,Q',
        '7,0,1,"McCarthy, Mr. Timothy J",male,54,0,0,17463,51.8625,E46,S',
        '8,0,3,"Palsson, Master. Gosta Leonard",male,2,3,1,349909,21.075,,S'
        ]

    assert work(lines) == (1, 0, 4, 0)
def test_work_3():
    lines = [
        '9,0,3,"Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)",male,27,0,2,347742,11.1333,,S',
        '10,1,2,"Nasser, Mrs. Nicholas (Adele Achem)",female,14,1,0,237736,30.0708,,C',
        '11,1,3,"Sandstrom, Miss. Marguerite Rut",female,4,1,1,PP 9549,16.7,G6,S'
    ]

    assert work(lines) == (0, 3, 2, 0)
