// function validate(e) {
//     console.log("here");
//     e.preventDefault();

//     var isvalid = true;
//     let name = document.forms["form"]["name"].value;
//     let pass = document.forms["form"]["password"].value;

//     document.getElementById("error").innerHTML = "";
//     document.getElementById("errorpas").innerHTML = "";

//     if (name === "") {
//         document.getElementById("error").innerHTML = "Name can't be empty";
//         console.log("empty");
//         isvalid = false;
//     } else if (name.length < 5) {
//         document.getElementById("error").innerHTML = "Name can't be less than 5 characters";
//         isvalid = false;
//     }

//     if (pass === "") {
//         document.getElementById("errorpas").innerHTML = "Password can't be empty";
//         isvalid = false;
//     } else if (pass.length < 7) {
//         document.getElementById("errorpas").innerHTML = "Password can't be less than 7 characters";
//         isvalid = false;
//     }

//     // Error message style
//     if (isvalid === false) {
//         document.getElementById("error").classList.add("display-block");
//         document.getElementById("errorpas").classList.add("display-block");
//     } else {
//         console.log(isvalid);
//         fetch(`/check-user/?username=${name}&password=${pass}`)
//             .then(response => response.json())
//             .then(data => {
//                 const messageElem = document.getElementById('message');
//                 messageElem.textContent = data.message;
//                 console.log(data);

//                 if (!data.exists) {
//                     // Submit the form (AJAX or traditional submission)
//                     document.forms["form"].submit(); // Uncomment if you want to submit after validation
//                 }
//             });
//     }
//     return false;
// }
