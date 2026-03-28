var data = [
    {
        "name": "Василий",
        "group": "912-2",
        "age": 19,
        "marks": [4, 3, 5, 5, 4]
    },
    {
        "name": "Анна",
        "group": "912-1",
        "age": 18,
        "marks": [3, 2, 3, 4, 3]
    },
    {
        "name": "Георгий",
        "group": "912-2",
        "age": 19,
        "marks": [3, 5, 4, 3, 5]
    },
    {
        "name": "Валентина",
        "group": "912-1",
        "age": 18,
        "marks": [5, 5, 5, 4, 5]
    }
]
let group = '912-1'
console.log(data)
console.table(data)

let filteredGroups = ()=>{
    console.log(group);

    if (group != '') {
        let memo = data.filter((element)=>{
            if (element.group == group) {
                return element
            }
        })
        console.log('------------------------------------------------------------------------')
        console.log(memo)
        console.table(memo)
        return memo ?? []
    }else
    {
        return data
    }
}

filteredGroups()