const searchField = document.querySelector(".search_input");
console.log(searchField);
searchField.addEventListener("keyup", (event) => {
  const search = event.target.value;
  const table = document.querySelector(".ul-table");
  table.innerHTML = "";
  console.log(search);
  if (search != " " && search.length > 0) {
    fetch("/capexout", {
      method: "POST",
      body: JSON.stringify({ sku: search }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        console.log(data["search"]);
        skus = data["search"].length;
        table.innerHTML = "";
        const drop = document.querySelector(".rowadrop");
        drop.style.display = "flex";
        myElement=document.getElementById("hidden");
        for (let i = 0; i < skus; i++) {
          myElement.style.display="flex";
          let sku = data["search"][i];
          console.log(JSON.stringify(sku.Description));
          var id = sku.id;
          table.innerHTML +=
            '<li class = "list-table"onclick="myfunc(' +
            id +
            ')">' +
            sku.Description +
            "</li>";
        }

        // const table = document.querySelector('.capexout-table');
        // for (let i = 0; i < data.length; i++)
        //     table.innerHTML = '<p>${data.sku}</p>';
      });
  }
  else{
    myElement=document.getElementById("hidden");
    myElement.style.display="none";
  }
});
function myfunc(id) {
  var url = "dashboard?search=" + encodeURIComponent(id);
  window.location.href = url;
}
function myfunc1() {
  var url = "dashboard?search1=" + encodeURIComponent(searchField.value);
  window.location.href = url;
}
function myfunc2(id) {
  var amount=document.getElementById(id).value;
  if(amount<1){
    alert("Please enter a Valid amount");
    return false;
  }
// Function to add elements to session storage

  // Retrieve the existing data from session storage
  const existingData = sessionStorage.getItem(id);
  if(existingData){
    sessionStorage.removeItem(id);
  }

  // Parse the existing data (if any) as an array or create an empty array if no data exists
  const dataArray = [];

  // Append the new value to the array
  dataArray.push(id,amount);

  // Convert the updated array back to a JSON string and store it in session storage
  sessionStorage.setItem(id, dataArray);
  display();

  // Function to get all data from session storage

 // Return the object containing all session storage data
}
 function display(){

  // Iterate over each key in sessionStorage
  const mytable=document.getElementById("mytable")
  for (let i = 0; i < sessionStorage.length; i++) {
    const key = sessionStorage.key(i);
    const value = sessionStorage.getItem(key);
    mytable.innerHTML +="<tr id="+i+'></tr>';
    for(let k=0;k<value.length;k+=2){
      const myrow=document.getElementById(i);
      if(k===0){
      }
    }
 }
 }




