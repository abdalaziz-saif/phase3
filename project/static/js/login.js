function validate(){

var isvalid = true;
   let name =  document.forms["form"]['name'].value;
   let pass=  document.forms["form"]['password'].value;
//    console.log(name);
   document.getElementById("error").innerHTML = "";
   document.getElementById("errorpas").innerHTML = ""

if (name==="" ){
document.getElementById("error").innerHTML ="name can't be empty";

isvalid = false;


}
 if (name.length<5){
    document.getElementById("error").innerHTML ="name can't be less than 5 charcter";
  
    
    isvalid = false;
}

if(pass==="")
{
    document.getElementById("errorpas").innerHTML ="password can't be empty";

    isvalid = false;
}
if (pass.length < 7){
        document.getElementById("errorpas").innerHTML ="password can't be less than 7 charcter";
        isvalid = false;
    }
//error message style
if (isvalid== false){
    document.getElementById("error").classList.add("display-block");
    document.getElementById("errorpas").classList.add("display-block");
}
//  ajax
if(isvalid){
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "users.json", true);


    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            const data = JSON.parse(xhr.responseText);
           

            // Check if the username and password match 
            let authenticated = false;

            for (let i = 0; i < data.users.length; i++) {
                if (data.users[i].username === username && data.users[i].password === password) {
                    authenticated = true;
                    break;
                }
            }

            const responseElement = document.getElementById("response");
            if (authenticated) {
                responseElement.innerText = "Authentication successful!";
                responseElement.style.color = "green";
                isvalid = true;
            } else {
                responseElement.innerText = "Invalid username or password.";
                responseElement.style.color = "red";
                isvalid = false;

            }

        }
        else if (xhr.readyState === 4 && xhr.status !== 200) {
            console.error("Error loading the JSON file." + xhr.status);
        }
   
       
}
xhr.send();

}

return isvalid;
}