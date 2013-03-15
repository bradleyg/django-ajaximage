$(function(){

  var attach = function($fileInput, upload_url, el){

    $fileInput.fileupload({
      url: upload_url,
      formData: {},
      dataType: 'json',
      paramName: 'file',

      add: function(e, data){
        $(el).attr('class', 'ajaximage progress-active')
        
        var regex = /jpg|jpeg|png|gif/i
        
        if( ! regex.test(data.files[0].type)){
          $(el).attr('class', 'ajaximage form-active')
          return alert('Incorrect image format. Allowed (jpg, gif, png).')
        }
        
        data.submit()
      },

      progress: function(e, data){
        var progress = parseInt(data.loaded / data.total * 100, 10)
        $(el).find('.bar').css({width: progress + '%'})
      },

      error: function(e, data){
        alert('Oops, file upload failed, please try again')
        $(el).attr('class', 'ajaximage form-active')
      },

      done: function(e, data){
        $(el).find('.link').attr('href', data.result.url)
        $(el).find('img').attr('src', data.result.url)
        $(el).attr('class', 'ajaximage img-active')
        $(el).find('input[type=hidden]').val(data.result.url)
        $(el).find('.bar').css({width: '0%'})
      }
    })
  }
  
  var setup = function(el){
    var upload_url = $(el).data('url')
    var img_url = $(el).find('input[type=hidden]').val()
    var $fileInput = $(el).find('input[type=file]')
    
    var class_ = (img_url === '') ? 'form-active' : 'img-active'
    $(el).attr('class', 'ajaximage ' + class_)
    
    $(el).find('.remove').click(function(e){
      e.preventDefault()
      $(el).find('input[type=hidden]').val('')
      $(el).attr('class', 'ajaximage form-active')
    })
    
    attach($fileInput, upload_url, el)
  }

  $('.ajaximage').each(function(i, el){
    setup(el)
  })
  
  $(document).bind('DOMNodeInserted', function(e) {
    var el = $(e.target).find('.ajaximage').get(0)
    var yes = $(el).length !== 0
    if(yes) setup(el)
  })

})