const dateField = document.querySelector('.date-field');
dateField.addEventListener('change', (event) => {
    console.log(event.target.value);
    const date = event.target.value;
    if  (date !== ''){
    fetch('/management_system/stockview', {
        method: 'POST',
        body: JSON.stringify({date: date}),
    })
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        const table = document.querySelector('.opening-stock-table');
        const tab = document.querySelector('.closing-stock-table');
        table.innerHTML = '<p>${data.opening_stock}</p>';
        tab.innerHTML = '<p>${data.closing_stock}</p>';
    })
}

});