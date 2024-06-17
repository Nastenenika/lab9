from main import get_data, work

def test_get_data():
    # Тест с простым примером данных
    test_lines = [
        "Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked\n",
        "1,1,Allen,Miss Elisabeth Walton,female,29,0,0,24160,211.3375,B5,S\n",
        "0,3,Moran,Mr. James,male,,0,0,330877,8.4583,,Q\n"
    ]
    with open('test_data.csv', 'w') as f:
        f.writelines(test_lines)

    result = get_data('test_data.csv')
    expected = [
        "1,1,Allen,Miss Elisabeth Walton,female,29,0,0,24160,211.3375,B5,S\n",
        "0,3,Moran,Mr. James,male,,0,0,330877,8.4583,,Q\n"
    ]
    assert result == expected, f"Expected {expected}, but got {result}"

def test_work_empty():
    lines = []
    result = work(lines)
    expected = (0, 0, 0, 0)  # No data
    assert result == expected, f"Expected {expected}, but got {result}"

def test_work_2():
    lines = [
        '6,1,3,"Moran, Mr. James",male,,0,1,330877,8.4583,,Q',
        '7,0,1,"McCarthy, Mr. Timothy J",male,54,0,0,17463,51.8625,E46,S',
        '8,0,3,"Palsson, Master. Gosta Leonard",male,2,3,1,349909,21.075,,S'
        ]

    assert work(lines) == (1, 0, 4, 0)


if __name__ == '__main__':
    test_get_data()
    test_work_empty()
    test_work_2()
