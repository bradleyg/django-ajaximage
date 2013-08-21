var $ajaxImage = jQuery.noConflict()

$ajaxImage(function(){

  var attach = function($fileInput, upload_url, el){

    $fileInput.fileupload({
      url: upload_url,
      formData: {},
      dataType: 'json',
      paramName: 'file',

      add: function(e, data){
        $ajaxImage(el).attr('class', 'ajaximage progress-active')
        
        var regex = /jpg|jpeg|png|gif/i
        
        if( ! regex.test(data.files[0].type)){
          $ajaxImage(el).attr('class', 'ajaximage form-active')
          return alert('Incorrect image format. Allowed (jpg, gif, png).')
        }
        
        data.submit()
      },

      progress: function(e, data){
        var progress = parseInt(data.loaded / data.total * 100, 10)
        $ajaxImage(el).find('.bar').css({width: progress + '%'})
      },

      error: function(e, data){
        alert('Oops, file upload failed, please try again')
        $ajaxImage(el).attr('class', 'ajaximage form-active')
      },

      done: function(e, data){
        $ajaxImage(el).find('.link').attr('href', data.result.url)
        $ajaxImage(el).find('img').attr('src', data.result.url)
        $ajaxImage(el).attr('class', 'ajaximage img-active')
        $ajaxImage(el).find('input[type=hidden]').val(data.result.filename)
        $ajaxImage(el).find('.bar').css({width: '0%'})
      }
    })
  }
  
  var setup = function(el){
    var upload_url = $ajaxImage(el).data('url')
    var img_url = $ajaxImage(el).find('input[type=hidden]').val()
    var $fileInput = $ajaxImage(el).find('input[type=file]')
    
    var class_ = (img_url === '') ? 'form-active' : 'img-active'
    $ajaxImage(el).attr('class', 'ajaximage ' + class_)
    
    $ajaxImage(el).find('.remove').click(function(e){
      e.preventDefault()
      $ajaxImage(el).find('input[type=hidden]').val('')
      $ajaxImage(el).attr('class', 'ajaximage form-active')
    })
    
    attach($fileInput, upload_url, el)
  }

  $ajaxImage('.ajaximage').each(function(i, el){
    setup(el)
  })
  
  $ajaxImage(document).bind('DOMNodeInserted', function(e) {
    var el = $ajaxImage(e.target).find('.ajaximage').get(0)
    var yes = $ajaxImage(el).length !== 0
    if(yes) setup(el)
  })

})