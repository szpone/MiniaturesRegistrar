var csrftoken = document.querySelector('input[name=csrfmiddlewaretoken]').value;

document.addEventListener("DOMContentLoaded", function(event) {
   var btnSubmit = document.querySelector("#save");
   var allLi = document.querySelectorAll('li.list-group-item');

   btnSubmit.addEventListener("click", function(event) {
     var data = [];
     for (var i = 0; i < allLi.length; i++) {
       var li = allLi[i];
       var allSelects = li.querySelectorAll('select');
       var liValues = [];
       for (var j = 0; j < allSelects.length; j++) {
         liValues.push(allSelects[j].value);
       }
       data.push(liValues);
     }
     console.log(JSON.stringify(data));
     var minInput = document.querySelector("#miniature-id");
     var minId = minInput.value;
     // send ajax
     $.ajax(
       {
         url: "/element_view/" + minId,
         data: {
           colors: JSON.stringify(data),
           csrfmiddlewaretoken: csrftoken,
         },
         method: "POST",
         dataType: 'json',
       }
     ).done(
       function (json) {
         console.log(json);
       }
     );
   });
});
