const video = document.getElementById('video-id');
if(video !== null){
    video.addEventListener('change', function(){
        if(this.files && this.files[0]){
            var reader = new FileReader();
            reader.onload = function(e){
                document.getElementById('vid').setAttribute('src', e.target.result);
            };
            reader.readAsDataURL(this.files[0]);
        }
    });
}