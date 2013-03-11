var initUpload = function(id, opts){
  var $el = $('#' + id)
  var name = $el.attr('name')
  var url = $el.val()
  
  if(url === ''){
    insertFileInput(name, id)
    attachHandler(name, id, opts)
  }
  else {
    insertImage(url, name, id)
  }
}

var insertImage = function(url, name, id){
  var $img = $('<img/>')
  $img.attr({'src': url}).addClass('ajaxupload')
  var $input = $('<input/>')
  $input.attr({
    name: name,
    id: id,
    value: url,
    type: 'hidden'
  })
  $('#' + id).replaceWith($img)
  $input.insertAfter($img)
}

var insertFileInput = function(name, id){
  var $input = $('<input/>')
  $input.attr({
    name: name,
    id: id,
    type: 'file'
  })
  $('#' + id).replaceWith($input)
}

var insertLoader = function(id){
  var $bar = $('<div/>')
  $bar.addClass('bar')
  
  var $progress = $('<div/>')
  $progress.addClass('ajaxupload progress progress-striped active')
  $progress.attr('id', id)
  
  $progress.append($bar)
  $('#' + id).replaceWith($progress)
}

var addFile = function(data, id){
  var allowed = ['jpeg', 'jpg', 'png', 'git']
  var ext = data.files[0].name.split('.').pop()

  if($.inArray(ext, allowed) === -1){
    return alert('You can only upload files with the following extension:\n.jpeg, .jpg, .png, .gif')
  }
  
  insertLoader(id)
  data.submit()
}

var updateProgress = function(e, data){
  var progress = parseInt(data.loaded / data.total * 100, 10)
  $('.ajaxupload .bar').css({width: progress + '%'})
}

var attachHandler = function(name, id, opts){
  var $input = $('#' + id + '[type=file]')

  $input.fileupload({
    url: opts.url,
    formData: {},
    replaceFileInput: false,
    paramName: 'file',
    add: function(e, data){
      addFile(data, id)
    },
    progress: updateProgress,
    done: function(e, data){
      insertImage(data.result, name, id)
    }
  })
}