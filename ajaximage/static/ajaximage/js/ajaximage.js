(function(){

    "use strict"

    var getCookie = function(name) {
        var value = '; ' + document.cookie,
            parts = value.split('; ' + name + '=')
        if (parts.length == 2) return parts.pop().split(';').shift()
    }

    var request = function(method, url, data, headers, el, showProgress, cb) {
        var req = new XMLHttpRequest()
        req.open(method, url, true)

        Object.keys(headers).forEach(function(key){
            req.setRequestHeader(key, headers[key])
        })

        req.onload = function() {
            cb(req.status, req.responseText)
        }

        req.onerror = req.onabort = function() {
            disableSubmit(false)
            error(el, 'Sorry, failed to upload image.')
        }

        req.upload.onprogress = function(data) {
            progressBar(el, data, showProgress)
        }

        req.send(data)
    }

    var parseJson = function(json) {
        var data
        try {data = JSON.parse(json)}
        catch(e){ data = null }
        return data
    }

    var progressBar = function(el, data, showProgress) {
        if(data.lengthComputable === false || showProgress === false) return

        var pcnt = Math.round(data.loaded * 100 / data.total),
            bar  = el.querySelector('.bar')

        bar.style.width = pcnt + '%'
    }

    var error = function(el, msg) {
        el.className = 'ajaximage form-active'
        el.querySelector('.file-path').value = ''
        el.querySelector('.file-input').value = ''
        alert(msg)
    }

    var update = function(el, data) {
        var link = el.querySelector('.file-link'),
            path = el.querySelector('.file-path'),
            img  = el.querySelector('.file-img')

        link.setAttribute('href', data.url)
        path.value = data.filename
        img.src = data.url

        el.className = 'ajaximage img-active'
        el.querySelector('.bar').style.width = '0%'
    }

    var concurrentUploads = 0
    var disableSubmit = function(status) {
        var submitRow = document.querySelector('.submit-row')
        if( ! submitRow) return

        var buttons = submitRow.querySelectorAll('input[type=submit]')

        if (status === true) concurrentUploads++
        else concurrentUploads--

        ;[].forEach.call(buttons, function(el){
            el.disabled = (concurrentUploads !== 0)
        })
    }

    var upload = function(e) {
        var el      = e.target.parentElement,
            file    = el.querySelector('.file-input').files[0],
            dest    = el.querySelector('.file-dest').value,
            form    = new FormData(),
            headers = {'X-CSRFToken': getCookie('csrftoken')},
            regex  = /jpg|jpeg|png|gif/i

        if( ! regex.test(file.type)){
            return alert('Incorrect image format. Allowed (jpg, gif, png).')
        }

        el.className = 'ajaximage progress-active'
        disableSubmit(true)
        form.append('file', file)

        request('POST', dest, form, headers, el, true, function(status, json){
            disableSubmit(false)

            var data = parseJson(json)

            switch(status) {
                case 200:
                    update(el, data)
                    break
                case 400:
                case 403:
                    error(el, data.error)
                    break;
                default:
                    error(el, 'Sorry, could not upload image.')
            }
        })
    }

    var removeUpload = function(e) {
        e.preventDefault()

        var el = e.target.parentElement
        el.querySelector('.file-path').value = ''
        el.querySelector('.file-input').value = ''
        el.className = 'ajaximage form-active'
    }

    var addHandlers = function(el) {
        var input  = el.querySelector('.file-input'),
            remove = el.querySelector('.file-remove'),
            path   = el.querySelector('.file-path'),
            status = (path.value === '') ? 'form' : 'img'

        el.className = 'ajaximage ' + status + '-active'

        remove.addEventListener('click', removeUpload, false)
        input.addEventListener('change', upload, false)
    }

    document.addEventListener('DOMContentLoaded', function(e) {
        ;[].forEach.call(document.querySelectorAll('.ajaximage'), addHandlers)
    })

    document.addEventListener('DOMNodeInserted', function(e){
        if(e.target.tagName) {
            var el = e.target.querySelector('.ajaximage')
            if(el) addHandlers(el)
        }
    })

})()