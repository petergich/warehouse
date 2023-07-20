const searchField = document.querySelector('.search_input');
console.log(searchField);
searchField.addEventListener('keyup', (event) => {
  const search = event.target.value;  
  console.log(search);
    if  (search !== ''){
    fetch('/capexout', {
        method: 'POST',
        body: JSON.stringify({sku: search}),
    }).then((response) => response.json())
      .then((data) => {
        console.log(data);
        // const table = document.querySelector('.capexout-table');
        // for (let i = 0; i < data.length; i++)
        //     table.innerHTML = '<p>${data.sku}</p>';
      })
    }
});