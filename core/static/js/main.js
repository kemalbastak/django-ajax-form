const form = document.getElementById('form-submit')

const csrf = document.getElementsByName('csrfmiddlewaretoken')
console.log(csrf)
const url = ""

$.ajax({
    type: 'POST',
    url: url,
    enctype: 'multipart/form-data',
    data: formData,
    success: function(response){
        console.log(response)
        const sText = `Form başarılı bir şekilde kaydedilmiştir`
    }
})