gsap.registerPlugin(ScrollTrigger);

gsap.set('.showcase button',{
    opacity:0,
    
});

const fadetl = gsap.timeline({
    ScrollTrigger:{
        scrub:true,
        
        
    }

});

fadetl.to(".showcase button", {
    opacity: 1,
    duration:2,
    y: 50,
    
});




