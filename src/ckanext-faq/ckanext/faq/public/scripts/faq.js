/* The Script for CivicData FAQs
 * @Author: Sion.qi
 * @Organization: MissionSky
 * @date: 2014-07-10
 * @version: v 1.0
*/
(function($) {
    $(document).ready(function() {
        var heading = $(".panel-heading");
        heading.each(function(e, idx) {
            $(this).click(function() {
                $(this).next().slideToggle();
            });
        });
    });
})(jQuery);