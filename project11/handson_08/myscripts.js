var employee = {
    name: "james Bond",
    job: "spy",
    age: 48,
    nameLength: function () {
        console.log(this.name.length);
        
    }
}

var employee = {
    name: "james Bond",
    job: "spy",
    age: 48,
    report: function() {
        alert("Name is"+this.name+", Job is"+this.job+", Age is"+this.age)
    }
}

var employee = {
    name: "james Bond",
    job: "spy",
    age: 48,
    lastname: function() {
        console.log(this.name.split(" "));
        
    }
}