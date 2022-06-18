function showMessage(input, message, type) {
	// get the small element and set the message
	const msg = input.parentNode.querySelector("small");
	msg.innerText = message;
	// update the class for the input
	input.className = type ? "success" : "error";
	return type;
}

function showError(input, message) {
	return showMessage(input, message, false);
}

function showSuccess(input) {
	return showMessage(input, "", true);
}

function hasValue(input, message) {
    // alert("hey there");
	if (input.value.trim() === "") {
		return showError(input, message);
	}
	return showSuccess(input);
}

function validateEmail(input, requiredMsg, invalidMsg) {
	// check if the value is not empty
	if (!hasValue(input, requiredMsg)) {
		return false;
	}
	// validate email format
	const emailRegex =
		/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

	const email = input.value.trim();
	if (!emailRegex.test(email)) {
		return showError(input, invalidMsg);
	}
	return true;
}
var userDetail = [
    {name:"sunil",age:"24",place:"delhi",avatar:"./image/abc.jpg",country:"India"},
    {name:"sujan",age:"22",place:"assam,",avatar:"./image/abc.jpg",country:"India"},
    {name:"abishek",age:"26",place:"kolkata",avatar:"./image/abc.jpg",country:"India"},
    {name:"chiranjeev",age:"20",place:"bangalore",avatar:"./image/abc.jpg",country:"India"},
]



const form = document.querySelector("#signup");

const NAME_REQUIRED = "Please enter your name";
const EMAIL_REQUIRED = "Please enter your email";
const EMAIL_INVALID = "Please enter a correct email address format";

form.addEventListener("submit", function (event) {
    console.log("submitted");
	// stop form submission
    // alert("hey");
	event.preventDefault();

	// validate the form
	let nameValid = hasValue(form.elements["name"], NAME_REQUIRED);
	let emailValid = validateEmail(form.elements["email"], EMAIL_REQUIRED, EMAIL_INVALID);
	// if valid, submit the form.
	if (nameValid && emailValid) {
		alert("Demo only. No form was posted.");
	}
});



document.getElementById('test1').innerHTML = userDetail.map(user => 
    `<div>
	<h1>hi</h1>
      <div>Name: ${user.name}</div>
      <div>Age: ${user.age}</div>
      <div>Place: ${user.place}</div>
      <div>Country: ${user.country}</div>
      <div>Avatar: ${user.avatar}</div>
    </div>`
).join('')

let count=5;

setInterval(displayHello, 15000);

function displayHello() {


// GET USERS
// fetch('http://127.0.0.1:5000/users')
// .then(function (response) {
//     console.log("here ",response.json)
//     return response.json();
// }).then(function (text) => {
//     console.log('GET response:');
//     console.log(type(text));
//     console.log(text); 
// });


// fetch('http://127.0.0.1:5000/users')
//   .then(response => response.json())
//   .then(data => console.log(data));
// //   .then(data => console.log(data));




// const requestOptions = {
//     method: 'POST',
//     headers: { 'Content-Type': 'application/json' },
//     body: JSON.stringify({ id:3 ,description:"testing", amount:9999  })
// };
// fetch('http://127.0.0.1:5000/make_request', requestOptions)
// .then(response=>console.log(response.json));

// console.log("my data ",data);

// fetch("http://127.0.0.1:5000/make_request", {
//   method: "post",
//   headers: {
//     'Accept': 'application/json',
//     'Content-Type': 'application/json',

//   },

//   //make sure to serialize your JSON body
//   body: JSON.stringify({
//     userid: 12,
//     description:"fdsfsdf",
//     amount:9999
//   })
// })
// .then( (response) => { 
//    //do something awesome that makes the world a better place
//    console.log(response);
// });
///////////////////////make request
// fetch("http://127.0.0.1:5000/make_request", {
//   method: "post",
//   headers: {
//     'Accept': 'application/json',
//     // "Content-Type": "text/plain"

//   },

//   //make sure to serialize your JSON body
//   body: JSON.stringify({
//     userid: 4,
//     description:"fdsfsdf",
//     amount:999
//   })
// })
// .then( function (response) { 
//    //do something awesome that makes the world a better place
//   console.log(response.json)
//    return response.json();
// })
// // .then(function(data){console.log("my data ",data)});
// .then((data) => {
//     // do stuff with responseJSON here...
//     console.log("my data", data['requestid']);

// })

/////////////delete request
fetch("http://127.0.0.1:5000/delete_request/", {
  method: "delete",
  headers: {
    'Accept': 'application/json',
    // "Content-Type": "text/plain"

  },

  //make sure to serialize your JSON body
  body: JSON.stringify({
    request_id: 97

  })
})
.then( function (response) { 
   //do something awesome that makes the world a better place
  console.log("my response ",response.ok)
   return response.ok; //response.ok==true means deletion was successful, no way to get return response?
})
// .then(function(data){console.log("my data ",data)});
.then((data) => {
    // do stuff with responseJSON here...
    console.log("my data", data);

})

}