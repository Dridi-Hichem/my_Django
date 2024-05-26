var firstName = prompt("Hello and welcome. What's your first name?")
var lastName = prompt("What's your last name?")
var age = prompt("What's your age?")
var height = prompt("What's your height in centimeters?")
var pet = prompt("What's your pet name?")
alert("Thank you for the information!")

var isSameFirstLetter = firstName[0] === lastName[0];
var isAgeRight = Number(age) > 20 && Number(age) < 30;
var isTallRight = Number(height) >= 170;
var isPetNameRight = pet[pet.length - 1] === "y"

if (isSameFirstLetter && isAgeRight && isTallRight && isPetNameRight) {
  console.log("Welcome Comorade! your mission code is 1518")
} else {
  console.log("Hello!")
}
