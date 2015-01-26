;(function($) {
 $(document).ready(function() {
        $.getJSON($("body").attr('data-site-root') + 'homepage_organizations', function(data) {
           if(data.success) {
               var result = data.result, html = "";
               for(var i=0; i<result.length; i++) {
                   var image = (result[i].image_url != '')? result[i].image_url : '/base/images/placeholder-organization.png';
                   html += "<div class='col-xs-2'><a href='/organization/" + result[i].name+ "' title='" + result[i].title+
                   "' class='thumbnail'><img src='" + image + "' alt='" + result[i].name+ "'></a></div>"
               }
               $("#who-publish").html(html);
           }
        });
    });
})(jQuery);

