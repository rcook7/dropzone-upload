(function () {
    var postCreateForm = document.getElementById('postCreateForm');

    Dropzone.autoDiscover = false;
    var myDropzone = new Dropzone("div#dropzone", {
        url: postCreateForm.action,
        autoProcessQueue: false,
        uploadMultiple: true,
        parallelUploads: 100,
        maxFiles: 100,
        init: function () {
            this.on("sendingmultiple", function (file, xhr, formData) {
                formData.append('csrfmiddlewaretoken', postCreateForm[0].value);
                formData.append('title', postCreateForm[1].value);
                console.log('send multiple files');
            });
            this.on("successmultiple", function (files, response) {
                window.location.href = response;
            });
            this.on("errormultiple", function (files, response) {
                window.location.href = response;
            });
        }
    });

    postCreateForm.addEventListener('submit', function(ev) {
        ev.preventDefault();
        ev.stopPropagation();


        myDropzone.processQueue();
    })
})();
