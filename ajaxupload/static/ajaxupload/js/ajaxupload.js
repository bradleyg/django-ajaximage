$(function(){
  
  var attach = function($fileInput, upload_url, el){
    
    $fileInput.fileupload({
      url: upload_url,
      formData: {},
      paramName: 'file',
      add: function(e, data){
        $(el).attr('class', 'ajaxupload progress-active')
        data.submit()
      },
      progress: function(e, data){
        var progress = parseInt(data.loaded / data.total * 100, 10)
        $(el).find('.bar').css({width: progress + '%'})
      },
      done: function(e, data){
        $(el).find('img').attr('src', data.result)
        $(el).attr('class', 'ajaxupload img-active')
        $(el).find('input[type=hidden]').val(data.result)
        $(el).find('.bar').css({width: '0%'})
      }
    })
  }
  
  $('.ajaxupload').each(function(i, el){
    var upload_url = $(el).data('url')
    var img_url = $(el).find('input[type=hidden]').val()
    var $fileInput = $(el).find('input[type=file]')
    
    var classs = (img_url === '') ? 'form-active' : 'img-active'
    $(el).attr('class', 'ajaxupload ' + classs)
    
    $(el).find('a').click(function(e){
      e.preventDefault()
      $(el).find('input[type=hidden]').val('')
      $(el).attr('class', 'ajaxupload form-active')
    })
    
    attach($fileInput, upload_url, el)
  })
  
})