// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array
function addNew() {
  var newName = prompt("Enter a new name:");
  roster.push(newName);
}

// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//
function remove(name) {
  var nameToRemove = prompt("Please enter the name to remove:");
  let index = roster.indexOf(nameToRemove);
  if (index > -1) {
    roster.splice(index, 1);
  }
}

// DISPLAY ROSTER

// Create a function called display that prints out the orster to the console.
function display() {
  console.log(roster);
}

// Start by asking if they want to use the web app
var answer = prompt("Would like to use the roster app? (y/n):");

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
if (answer == "y") {
  while (true) {
    var action = prompt("Please select an action: add, remove, display, quit:");

    if (action == "add") {
      addNew();
    } else if (action == "remove") {
      remove();
    } else if (action == "display") {
      display();
    } else if (action == "quit") {
      alert("You quitted roster!");
      break;
    } else {
      alert("Wrong choice!");
    }
  }
}

alert("Thank you for visiting!")
