function typeclick(w,t){
    var table=document.getElementById("table"+w);
    var table1=document.getElementById("table1"+w)
    while (table.firstChild) {
      table.removeChild(table.firstChild);
   }
    th=document.getElementById("head"+w);
    th1=document.getElementById("head1"+w);
    th.classList.remove("hidden");
    th1.classList.add("hidden");
      const elements = document.querySelectorAll('.warehouse');
      const inputs=document.querySelectorAll(".buy-now")
        const requestData = {
          warehouse: w,
          type: t
      };
      inputs.forEach(inp=>{
        inp.classList.add("hidden")
      });
  
      const queryParams = new URLSearchParams(requestData);
  
      fetch('dashboard?' + queryParams)
      .then(response => response.json())
      .then(data => {
        console.log(data)
        elements.forEach(element => {
          if (data.filtered!=[]){
  
          if (element.id ==w) {
            table.classList.remove('hidden');
            element.classList.remove('hidden'); // Show the specified element
          }
          else{
            element.classList.add('hidden');
      
          }
    
          // Hide other elements
          
        }
      });
      var dat=data.descriptions;
          dat.forEach(instance=>{
            row=document.createElement('tr');
            row.id=instance.description;
            row.style.cursor="pointer";
            row.classList.add('table1')
            row.addEventListener('click', function(event) {
              const btn=document.getElementById("button"+w)
              const po=document.getElementById("po"+w)
              const capex=document.getElementById("capex"+w)
              const quantity=document.getElementById("quantity"+w)
              const reason=document.getElementById("reason"+w)
              const inp=document.getElementById("input"+w)
              const clickedRow = event.target.closest('tr');
              const error=document.getElementById("error"+w)
              inp.classList.remove('hidden');
              th.classList.add('hidden');
              th1.classList.remove("hidden")
              while (table.firstChild) {
                table.removeChild(table.firstChild);
             }
             while (table1.firstChild) {
              table1.removeChild(table1.firstChild);
           }
              commodity(clickedRow,dat,table1,w,btn,po,capex,quantity,reason,error)
          });
            table.appendChild(row);
            var tables=document.querySelectorAll('.table1');
    
            des=document.createElement('td');
            quantity=document.createElement('td');
            packaging=document.createElement('td');
            // po=document.createElement('td');
            // pq=document.createElement('td');
            // price=document.createElement('td');
            row.appendChild(des);
            row.appendChild(quantity);
            row.appendChild(packaging);
            des.innerHTML=instance.description;
            quantity.innerHTML=instance.quantity;
            packaging.innerHTML=instance.pacaging;
          });
          // Process the retrieved data in your JavaScript code
          // For example, you can display it in the resultDiv
      })
      .catch(error => {
          console.error('Error:', error);
          alert("An error occured!Please try again");
          return false;
      });
    }
    function hide(){
      var elem = document.getElementById("hide");
      elem.remove();
      var elem2=document.getElementById("layout-navbar");
      elem2.remove();
    }
    function commodity(clickedRow,dat,table1,w,btn,po,capex,quantity,reason,error){
      if (clickedRow) {
          const clickedRowId = clickedRow.id;
          // var tables=document.querySelectorAll('.table1');
        if(w==="Safaricom"){
          po.addEventListener("input",function(){
            if(po.value!=""){
              dat.forEach(data=>{
                if(data.description===clickedRowId){
                  instances=data.chekins
                  const puo=[]
                  instances.forEach(ins=>{
                    puo.push(ins.purchase_order);
                  });
                  if (puo.includes(po.value)) {
                    error.classList.remove("hidden");
                    error.style.color="green";
                    error.innerHTML="Exists";
                    puo.forEach(p=>{
                      if(p===po.value){
                        selectedPO=po.value
                        order(selectedPO,btn,capex,quantity,reason,error,clickedRowId,puo,po)
                      }
                    });
                  } 
                  else {
                    error.classList.remove("hidden");
                    error.style.color="red"
                    error.innerHTML="! Purchase order does not exist "
                  }
                }
              });
            }
            else{
              error.innerHTML="";
              error.classList.add("hidden")
            }
          });
         dat.forEach(instanc=>{
          if(instanc.description===clickedRowId){
            var checkins=instanc.chekins
            count=0;
            checkins.forEach(che=>{
              row1=document.createElement("tr")
              table1.appendChild(row1);
              row1.classList.add("tablerow");
              if(che.description===clickedRowId){
                if(count===0){
                  count++
                  des1=document.createElement('td');
                  quantity1=document.createElement('td');
                  packaging1=document.createElement('td');
                  po1=document.createElement('td');
                  pq1=document.createElement('td');
                  pq1.id=instanc.description+che.purchase_order
                  pq1.value=che.quantity
                  price1=document.createElement('td');
                  row1.appendChild(des1);
                  row1.appendChild(quantity1);
                  row1.appendChild(packaging1);
                  row1.appendChild(po1);
                  row1.appendChild(pq1);
                  row1.appendChild(price1);
                  des1.innerHTML=instanc.description;
                  quantity1.innerHTML=instanc.quantity;
                  packaging1.innerHTML=instanc.pacaging;
                  if(che.purchase_order===null){
                    p01.innerHTML="null";
                  }
                  else{
                    po1.innerHTML=che.purchase_order;
                  }
                  pq1.innerHTML=che.quantity;
                  if(che.price===null){
                    price1.innerHTML="null";
                  }
                  else{
                  price1.innerHTML=che.price;
                  }
          // tables.forEach(tab=>{
          //   if (tab.id!=clickedRowId){
          //     tab.classList.add('hidden');
          //   }
                }
                else{
                  count++
                  des1=document.createElement('td');
                  quantity1=document.createElement('td');
                  packaging1=document.createElement('td');
                  po1=document.createElement('td');
                  pq1=document.createElement('td');
                  pq1.id=instanc.description+che.purchase_order
                  pq1.value=che.quantity
                  price1=document.createElement('td');
                  row1.appendChild(des1);
                  row1.appendChild(quantity1);
                  row1.appendChild(packaging1);
                  row1.appendChild(po1);
                  row1.appendChild(pq1);
                  row1.appendChild(price1);
                  des1.innerHTML='-';
                  quantity1.innerHTML='-';
                  packaging1.innerHTML="-";
                  if(che.purchase_order===null){
                    p01.innerHTML="null";
                  }
                  else{
                    po1.innerHTML=che.purchase_order;
                  }
                  pq1.innerHTML=che.quantity;
                  if(che.price===null){
                    price1.innerHTML="null";
                  }
                  else{
                  price1.innerHTML=che.price;
                  }
                }
              }
          });
          }
        });
      }
      else{
        po.classList.add("hidden");
        capex.classList.add("hidden");
        reason.classList.add("hidden");
        dat.forEach(instanc=>{
          if(instanc.description===clickedRowId){
              row1=document.createElement("tr")
              table1.appendChild(row1);
              row1.classList.add("tablerow");
                  des1=document.createElement('td');
                  quantity1=document.createElement('td');
                  packaging1=document.createElement('td');
                  po1=document.createElement('td');
                  pq1=document.createElement('td');
                  price1=document.createElement('td');
                  row1.appendChild(des1);
                  row1.appendChild(quantity1);
                  row1.appendChild(packaging1);
                  row1.appendChild(po1);
                  row1.appendChild(pq1);
                  row1.appendChild(price1);
                  des1.innerHTML=instanc.description;
                  quantity1.innerHTML=instanc.quantity;
                  packaging1.innerHTML=instanc.pacaging;
                  po1.innerHTML="null";
                  pq1.innerHTML="null";
                  price1.innerHTML="null";
          }
        });
      }
      }
    }
    function order(selectedPO,btn,capex,quantity,reason,error,clickedRowId,puo,po){
      field=document.getElementById(clickedRowId+selectedPO)
      original=field.value
      alert(original)
      quantity.addEventListener('input',function(){
        if(quantity.value!=0){
  
          value=field.innerHTML
          update=value-quantity.value
          if(update<0){
            error.style.color="red";
            error.innerHTML="! The quantity is not available from the capex"
          }
          else{
            if (puo.includes(po.value)){
            error.innerHTML="Exists"
            error.style.color="green"
            field.innerHTML=update;
            btn.addEventListener('click',function(){
              ca=capex.value
              re=reason.value
              or=error.innerHTML
              co=error.style.color
              if(ca===""&&re===""){
                error.style.color="red";
                error.innerHTML="!please enter a capex or reason for no capex";
              }
              else{
                error.innerHTML=or
                error.style.color=co
              }
            });
          }
          }
        }
        if(quantity.value===""){
          field.innerHTML=original
        }
      });
    }
    
  
  