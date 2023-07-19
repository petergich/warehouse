const searchField = document.querySelector('.search_input');
console.log(searchField);
searchField.addEventListener('keyup', (event) => {
    console.log(event.target.value);
    const search = event.target.value;
    if  (search !== ''){
    fetch('/management_system/capexout', {
        method: 'POST',
        body: JSON.stringify({sku: search}),
    }).then((response) => response.json())
      .then((data) => {
        console.log(data);
        const table = document.querySelector('.capexout-table');
        table.innerHTML = '<p>${data.sku}</p>';
      })
    }
});