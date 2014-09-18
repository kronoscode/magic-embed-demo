$(document).ready(function(){

    //footer
    $('.footer-arrow, .more-about-link').click(function(){
        $('.credits').slideToggle(100);
        $('.footer-arrow > i').toggleClass('fa-angle-down', 'fa-angle-up');
        $("html, body").animate({ scrollTop: $(document).height() }, 800);
        return false;
    })

    $( "form:first" ).submit(function( event ) {
        $('select').val($('.dd-selected-text').text());
        $('form:first').append($('select'));
    });
});
// Menu Overlay
(function() {
    var triggerBttn = document.getElementById( 'trigger-overlay' ),
        overlay = document.getElementById( 'main-overlay' ),
        closeBttn = overlay.querySelector( 'button.overlay-close' );
        transEndEventNames = {
            'WebkitTransition': 'webkitTransitionEnd',
            'MozTransition': 'transitionend',
            'OTransition': 'oTransitionEnd',
            'msTransition': 'MSTransitionEnd',
            'transition': 'transitionend'
        },
        transEndEventName = transEndEventNames[ Modernizr.prefixed( 'transition' ) ],
        support = { transitions : Modernizr.csstransitions };

    function toggleOverlay() {
        if( classie.has( overlay, 'open' ) ) {
            classie.remove( overlay, 'open' );
            var onEndTransitionFn = function( ev ) {
                if( support.transitions ) {
                    if( ev.propertyName !== 'visibility' ) return;
                    this.removeEventListener( transEndEventName, onEndTransitionFn );
                }
                classie.remove( overlay, 'close' );
            };
            if( support.transitions ) {
                overlay.addEventListener( transEndEventName, onEndTransitionFn );
            }
            else {
                onEndTransitionFn();
            }
        }
        else if( !classie.has( overlay, 'close' ) ) {
            classie.add( overlay, 'open' );            
        }
    }

    $('.trigger-overlay').each(function(id, trigger_btn){
        trigger_btn.addEventListener( 'click', toggleOverlay );
    });

    $('body').on('click', '.trigger-overlay', function(){
        var overlay = $('#main-overlay'),
            target_overlay = $(this).data('target-overlay'),
            selected_content = $("#overlays-content [data-overlay='" + target_overlay + "']").clone().html();
        
        // reset content
        var closebtn = overlay.find('button.overlay-close').detach()
        overlay.empty().append(closebtn);
        
        // add the right content according to click button
        overlay.append(selected_content);

        // contact form selects
        $('.overlay .contact-select').ddslick();

    });
    
    $('body').on('click', '.toggle-overlay-close', function() {
        toggleOverlay();
    });
})();