var groupmates = [
{
    "name": "Иванов",
    "group": "БСТ2257",
    "age": 20,
    "marks": [5,4,5,5,4]
},
{
    "name": "Петров",
    "group": "БСТ2257",
    "age": 21,
    "marks": [3,3,4,3,4]
},
{
    "name": "Сидоров",
    "group": "БСТ2257",
    "age": 20,
    "marks": [5,5,5,4,5]
},
{
    "name": "Кузнецов",
    "group": "БСТ2258",
    "age": 22,
    "marks": [4,3,3,4,3]
},
{
    "name": "Смирнова",
    "group": "БСТ2258",
    "age": 19,
    "marks": [4,5,4,5,4]
}
];

var rpad = function(str, length){
    str = str.toString();
    while (str.length < length)
        str = str + ' ';
    return str;
};

var printStudents = function(students){

    console.log(
        rpad("Имя студента",15),
        rpad("Группа",10),
        rpad("Возраст",10),
        rpad("Оценки",20)
    );

    for (var i = 0; i < students.length; i++){

        console.log(
            rpad(students[i]['name'],15),
            rpad(students[i]['group'],10),
            rpad(students[i]['age'],10),
            rpad(students[i]['marks'],20)
        );

    }

    console.log('\n');
};

var filterByAge = function(students, minAge){

    var result = [];

    for (var i = 0; i < students.length; i++){
        if (students[i]['age'] >= minAge){
            result.push(students[i]);
        }
    }

    return result;
};

printStudents(groupmates);

console.log("Студенты старше 20 лет:");

printStudents(filterByAge(groupmates,21));