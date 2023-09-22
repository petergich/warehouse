
var tables = document.getElementsByTagName('table');

function listGoods(client,project){
    const url = new URL('check', window.location.origin);
    url.searchParams.append('client', client);
    url.searchParams.append('project', project);

    fetch(url)
        .then(response => response.json())
        .then(data => {
            // Process the received data
            if(data==="found"){
                fetchData(client,project);
            }
            else{
                alert(data)
            }
        })
        .catch(error => {
            alert(error);
        });
}
function fetchData(client,project){
    url="selected?client="+encodeURIComponent(client)+"&project="+encodeURIComponent(project);
    window.location.href=url
}
function desSelect(client,project,des,qty){
    url="good?client="+encodeURIComponent(client)+"&project="+encodeURIComponent(project)+"&description="+encodeURIComponent(des)+"&quantity="+encodeURIComponent(qty);
    window.location.href=url;
}
// container.addEventListener('mouseover', function(event) {
//     const hoveredDiv = event.target;
//     const dropdownId = document.getElementById("client"+hoveredDiv.id);
//     if (dropdownId) {
//         dropdownId.style.display = 'block';
//     }
// });
// container.addEventListener('mouseout', function(event) {
//     const hoveredDiv = event.target;
//     const dropdownId=document.getElementById("client"+hoveredDiv.id);
//     if (dropdownId) {
//         dropdownId.style.display = 'none';
//     }
// });
// const container = document.querySelector('.clients');
// const allelement=document.querySelectorAll(".float-parent")
// container.addEventListener('click', function(event) {
//     const hoveredDiv = event.target;
//     const dropdownId=document.getElementById("client"+hoveredDiv.id);
//     // allelement.forEach(element=>{
//     //     if(element.id){
//     //     if(element.id!=dropdownId.id){

//     //     element.style.display="none";
//     //     }
//     // }
        
//     // });
//     if (dropdownId) {
//         dropdownId.style.display="block";
//     }
// });
// Function to fetch data from the server
// const dateField = document.querySelector('.opening_stock');
// const DateField = document.querySelector('.closing_stock');
// dateField.addEventListener('change', (event) => {
//     const dateVal = event.target.value;
//     console.log(dateVal);
//     let json = JSON.stringify({openingdate :dateVal});
//     console.log(json);
//     if  (dateVal.length > 0 ){
//         var url = "dashboardstock/?openingdate=" + encodeURIComponent(dateVal);
//         window.location.href = url;
       
// }

// });
// DateField.addEventListener('change', (event) => {
//     const dateVal = event.target.value;
//     if  (dateVal.length > 0 ){
//         var url = "dashboardstock/?closingdate=" + encodeURIComponent(dateVal);
//         window.location.href = url;
       
// }

// });
// function hide(){
//     alert("called")
//     elements=document.querySelectorAll(".hide")
//     elements.forEach(element => {
//         element.classList.add("hidden")
//     });
// }









