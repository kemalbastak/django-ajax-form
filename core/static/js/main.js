const form = document.getElementById('form-submit')

const csrf = document.getElementsByName('csrfmiddlewaretoken')

const header = document.getElementById('id_header')
const description = document.getElementById('id_description')
const link = document.getElementById('id_link')
const email = document.getElementById('id_email')
const image = document.getElementById('id_image')
const uuid_input = document.getElementById('id_uuid')
const alertBox = document.getElementById('alert-box')
var imgBox = document.getElementById('img-box')




image.addEventListener('change', ()=>{
    const img = image.files[0]
    const url = URL.createObjectURL(img)
    imgBox.innerHTML = `<img src="${url}"  width="100"/>`
    console.log(imgBox)
})

const handleAlerts = (type, text) => {
    alertBox.innerHTML = `<div class="alert alert-${type}" role="alert">
    ${text}
  </div>`
}

form.addEventListener('submit', e=>{
    e.preventDefault()
    function uuidv4() {
        return ([1e7]+-1e3+-4e3+-8e3+-1e11).replace(/[018]/g, c =>
          (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
        );
      }
    uuid = uuidv4() 
    const url = ""
    const formData = new FormData()
    formData.append('csrfmiddlewaretoken', csrf[0].value)
    formData.append('header', header.value)
    formData.append('description', description.value)
    formData.append('link', link.value)
    formData.append('email', email.value)
    formData.append('image', image.files[0])
    formData.append('uuid', uuid)
    for (var key of formData.entries()) {
        console.log(key[0] + ', ' + key[1]);
    }

    $.ajax({
        type: 'POST',
        url: url,
        enctype: 'multipart/form-data',
        data: formData,
        success: function(response){
            var href = window.location.href
            if (href.includes("/tr/")) {
                uuidBox.innerHTML = handleAlerts("primary", `Kullanıcı kodunuz buradadır : ${uuid}`)
            }
            else if(href.includes("/en/")){
                uuidBox.innerHTML = handleAlerts("primary", `User code is here: ${uuid}`)
            }

        },
        error: function(response){
            var href = window.location.href
            if (href.includes("/tr/")) {
                uuidBox.innerHTML = handleAlerts("danger", "Hata... Formu gönderirken bir hata oluştu.")
            }
            else if(href.includes("/en/")){
                uuidBox.innerHTML = handleAlerts("danger", "Error... An error occured while sending the form.")
            }


        },
        processData: false,
        contentType: false,
    })
})

