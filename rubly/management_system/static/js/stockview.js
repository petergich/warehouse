const dateField = document.querySelector('.opening_stock');
const DateField = document.querySelector('.closing_stock');
dateField.addEventListener('change', (event) => {
    const dateVal = event.target.value;
    console.log(dateVal);
    let json = JSON.stringify({date :dateVal});
    console.log(json);
    if  (dateVal.length > 0 ){
        fetch('/dashboardstock', {
            body: json,
            method: 'POST',
    })
    .then((res) => res.json())
    .then((data) => {
        console.log('data',data);
        // const table = document.querySelector('.opening-stock-table');
        // const tab = document.querySelector('.closing-stock-table');
        // table.innerHTML = '<p>${data.opening_stock}</p>';
        // tab.innerHTML = '<p>${data.closing_stock}</p>';
    })
}

});
DateField.addEventListener('change', (event) => {
    const dateVal = event.target.value;
    console.log(dateVal);
    let json = JSON.stringify({date :dateVal});
    console.log(json);
    if  (dateVal.length > 0 ){
        fetch('/dashboardstock', {
            body: json,
            method: 'POST',
    })
    .then((res) => res.json())
    .then((data) => {
        console.log('data',data);
        // const table = document.querySelector('.opening-stock-table');
        // const tab = document.querySelector('.closing-stock-table');
        // table.innerHTML = '<p>${data.opening_stock}</p>';
        // tab.innerHTML = '<p>${data.closing_stock}</p>';
    })
}

})