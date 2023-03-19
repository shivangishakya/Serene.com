<template>
    <div style="z-index: 1000; position: relative;">
        <div class=" mwblock__background--top-banner ">
            <div class="container">
                <div class="mwblock mwblock--top-banner">
                    <div class="mwblock__caption" style="cursor: pointer; color: rgb(50, 15, 47);">
                        <img src="../assets/serenelogo.png">
                        <h1>{{ msg }}</h1>
                    </div>
                </div>
                <!-- ::after -->
            </div>
        </div>
    </div>
    <nav id="js-header" class="navbar__wrap  navbar__wrap--has-meta ">
        <div class="navbar">
            <div class="pull-left">
                <a  @click="showCategories=!(showCategories);" href="#" class="navbar__categories icon-icon-category">MENU</a>
                <!-- <h1 v-if="!showCategories">Hide me on click event!</h1> -->
            </div>
        </div>
    </nav>
    <div class="site-content">
        <div class="description">
            <p>
                <br><br>HELLO STUDENTS!!!<br><br>Mental health problems can impact the academic performance and success of a college student. <br><br>
                Campus-wide mental health resources for students to seek support could be the key to their academic success.<br><br>
                Don't Worry about Anything. SERENE will help you to track your stress level<br><br>
                Track your mental health by calculating your stress levels in just few minutes.<br>
                So Start Now!!!<br><br>
                <a href="http://localhost:3000/login/" target="_blank" rel="noopener">BEGIN NOW</a>.
            </p>
        </div>
        <div class="calmlink">
            <p>
                For series of calmness in your life, check out the
                <a href="https://www.youtube.com/watch?v=pBoAquxhspA" target="_blank" rel="noopener">Calm Videos</a>.
            </p>
        </div>
    </div>
    <categories v-if="!showCategories">
        <!-- <h1> Hide me on click event!</h1> -->
    <!-- <categories v-model="showCategories" inline-template></categories> -->
     <div class='categories--is-active'>
        <div class="categories__backdrop"></div>
        <div class="categories__wrap">
            <button @click="showCategories = !showCategories" id="js-categories__close" class="categories__close">
                <svg width="25px" height="25px" view-box="0 0 25 25" version="1.1" xmlns="http://www.w3.org/2000/svg" xmnls:xlink="http://www.w3.org/1999/xlink" class="svg-inline icon-close">
                    <title>icon-close</title>
                    <desc>Created with sketch.</desc>
                    <defs></defs>
                    <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                        <g id="Icons" transform="translate(-426.000000, -13.000000)" fill-rule="nonzero" fill="#40BB84">
                            <path d="M426.39576,37.6042403 C426.924096,38.1319199 427.780003,38.1319199 428.308339,37.6042403 L438.516282,27.3962977 L448.724224,37.6042403 C449.257419,38.1010759 450.088308,38.0864158 450.603644,37.5710801 C451.11898,37.0557445 451.13364,36.224855 450.636804,35.6916607 L440.428861,25.4837181 L450.636804,15.2757756 C451.13364,14.7425813 451.11898,13.9116918 450.603644,13.3963561 C450.088308,12.8810204 449.257419,12.8663603 448.724224,13.3631959 L438.516282,23.5711385 L428.308339,13.3631959 C427.775145,12.8663603 426.944256,12.8810204 426.42892,13.3963561 C425.913584,13.9116918 425.898924,14.7425813 426.39576,15.2757756 L436.603702,25.4837181 L426.39576,35.6916607 C425.86808,36.2199974 425.86808,37.0759036 426.39576,37.6042403 Z" id="icon-close"></path>
                        </g>
                    </g>
                </svg>
            </button>
            <div class="categories__wrap-inner">
                <ul class="categories__menu">
                    <li class="animated tag--58 categories__menu-item slideInUp">
                        <a href="#" class="categories__menu-link">About Us</a>
                    </li>
                    <li class="animated tag--62 categories__menu-item slideInUp">
                        <a href="#" class="categories__menu-link">Register</a>
                    </li>
                    <li class="animated tag--58 categories__menu-item slideInUp">
                        <a href="#" class="categories__menu-link">Login</a>
                    </li>
                    <li class="animated tag--58 categories__menu-item slideInUp">
                        <a href="#" class="categories__menu-link">Contact Us</a>
                    </li>
                </ul>
            </div>
        </div>
    </div>
    </categories>
  </template>
  
  <script>
  export default {
    name: "Homepage",
    props: {
      msg: String,
    },
    data: ()=>({
        showCategories : true
    }),
    methods:{
    }
  };
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  a:-webkit-any-link {
    color: -webkit-link;
    cursor: pointer;
    text-decoration: underline;
}
    .categories__menu-item a.categories__menu-link {
        transition: all .2s ease-out;
        line-height: 60px;
        font-size: 22px;
        font-weight: 700;
        color: #435b71;
        text-decoration: none;
        border-radius: 30px;
        display: inline-block;
        width: 100%;
        height: 60px;
    }
    a {
        color: #293948;
        text-decoration: none;
    }
    a:hover {
        background-color:darksalmon;
        cursor: pointer;
    }
    .animated {
        -webkit-animation-duration: 1s;
        animation-duration: 1s;
        -webkit-animation-fill-mode: both;
        animation-fill-mode: both;
    }
    .categories__menu-item {
        margin-bottom: 12px;
        -webkit-animation-duration: .4s;
        animation-duration: .4s;
    }
    .slideInUp {
        -webkit-animation-name: slideInUp;
        animation-name: slideInUp;
    }
    .animated {
        -webkit-animation-duration: 1s;
        animation-duration: 1s;
        -webkit-animation-fill-mode: both;
        animation-fill-mode: both;
    }
    li {
        display: list-item;
        text-align: -webkit-match-parent;
    }
    .categories__wrap-inner {
        padding: 30px 40px;
        position: relative;
    }
    .categories__menu {
        padding: 0;
        list-style-type: none;
        text-align: center;
        margin: 45px 0 30px;
    }
    ul {
        margin-top: 0;
        margin-bottom: 11px;
    }
    ul {
        display: block;
        list-style-type: disc;
        margin-block-start: 1em;
        margin-block-end: 1em;
        margin-inline-start: 0px;
        margin-inline-end: 0px;
        padding-inline-start: 40px;
    }
    .animated {
        -webkit-animation-duration: 1s;
        animation-duration: 1s;
        -webkit-animation-fill-mode: both;
        animation-fill-mode: both;
    }
    .categories--is-active .categories__wrap {
        left: 0;
    }
    .categories__wrap {
        transition: all .6s ease-in;
        background-color: #fff;
        position: fixed;
        left: -100%;
        top: 0;
        width: 100%;
        max-width: 430px;
        z-index: 5000;
        box-shadow: 0 2px 3px 0 rgb(0 0 0 / 46%);
        height: 100%;
        overflow-y: auto;
        overflow-x: hidden;
    }

    .categories__close {
        background: none;
        border: none;
        position: absolute;
        right: 30px;
        top: 20px;
        cursor: pointer;
        z-index: 100;
        padding: 10px;
        line-height: 0;
    }
    button, input, select, textarea {
        font-family: inherit;
        font-size: inherit;
        line-height: inherit;
        text-transform: none;
        overflow: visible;
        color: inherit;
        font: inherit;
        margin: 0;
    }
    button, html input[type=button], input[type=reset], input[type=submit] {
        -webkit-appearance: button;
        cursor: pointer;
    }
    .svg-inline {
        display: inline-block;
        vertical-align: middle;
    }
    svg:not(:root) {
        overflow: hidden;
    }
    :not(svg) {
        transform-origin: 0px 0px;
    }

    .categories--is-active .categories__backdrop {
        opacity: 1;
        filter: alpha(opacity=100);
        visibility: visible;
        cursor: pointer;
    }
    .categories__backdrop{
        visibility: hidden;
        transition: all .3s ease-in;
        opacity: 0;
        filter: alpha(opacity=0);
        z-index: 4900;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(67,91,113,.5);
    }
    *, :after {
        box-sizing: border-box;
    }
    h1 {
        text-align: left;
        font-family:'Quicksand','Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
        font-style: oblique;
        font-stretch: expanded;
        color:teal;
        text-decoration-style: dashed;
        /* background-color:goldenrod; */
    }
    .calmlink {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 30%;
        margin-right: auto;
        margin-left: 30px;
    }
    .description {
        margin-top: 0;
        margin-left: 30px;
        text-align: left;
        margin-right: auto;
        display: flex;
        width: 30%
    }
    .mwblock__background--top-banner {
        background: white;
    }
    .mwblock__background--top-banner {
        border-bottom: 1px solid #fff;
        border-bottom-width: 1px;
        border-bottom-style: solid;
        border-bottom-color: rgb(255, 255, 255);
    }
    .mwblock--top-banner {
        padding-right: 10px;
        -moz-justify-content: space-between;
        justify-content: space-between;
        -moz-flex-direction: row;
        flex-direction: row;
    }
    .container {
        margin-right: auto;
        margin-left: auto;
        padding-left: 15px;
        padding-right: 15px;
    }
    img {
        max-height: 100px;
        max-width: 200px;
        vertical-align: left;
        border: 50;
    }
    img {
        overflow-clip-margin: content-box;
    }
    .mwblock__caption {
        margin-top: 0;
        margin-left: 10px;
        text-align: left;
        margin-right: auto;
        display: flex;
        justify-content: center;
    }
    .navbar__wrap {
        height: auto!important;
        position: static!important;
        margin-bottom: 10px!important;
    }
    .navbar {
        position: relative;
        height: 80px;
        width: 100%;
        background-color: gainsboro;
        box-shadow: 0 2px 3px 0 rgb(0 0 0 / 16%);
    }
    .pull-left {
        float: left!important;
    }
    .navbar__categories {
        font-size: 14px;
        line-height: 80px;
        font-size: 12px;
        padding-right: 30px;
        display: inline-block;
        text-align: center;
        font-weight: 700;
        text-decoration: none;
        text-transform: uppercase;
        background-position: center left 30px;
        background-repeat: no-repeat;
        padding-left: 70px;
    }
    .icon-icon-category {
        background-image: url(data:image/svg+xml;charset=US-ASCII,%3C%3Fxml%20version%3D%221.0%22%20encoding%3D%22UTF-8%22%3F%3E%0A%3Csvg%20width%3D%2222px%22%20height%3D%2220px%22%20viewBox%3D%220%200%2022%2020%22%20version%3D%221.1%22%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20xmlns%3Axlink%3D%22http%3A//www.w3.org/1999/xlink%22%3E%0A%20%20%20%20%3C%21--%20Generator%3A%20Sketch%2046.2%20%2844496%29%20-%20http%3A//www.bohemiancoding.com/sketch%20--%3E%0A%20%20%20%20%3Ctitle%3Eicon-category%3C/title%3E%0A%20%20%20%20%3Cdesc%3ECreated%20with%20Sketch.%3C/desc%3E%0A%20%20%20%20%3Cdefs%3E%3C/defs%3E%0A%20%20%20%20%3Cg%20id%3D%22Page-1%22%20stroke%3D%22none%22%20stroke-width%3D%221%22%20fill%3D%22none%22%20fill-rule%3D%22evenodd%22%3E%0A%20%20%20%20%20%20%20%20%3Cg%20id%3D%22Icons%22%20transform%3D%22translate%28-285.000000%2C%20-203.000000%29%22%20fill-rule%3D%22nonzero%22%20fill%3D%22%23435B71%22%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Cpath%20d%3D%22M306.101993%2C221.686987%20C306.101993%2C222.413834%20305.515826%2C223%20304.78898%2C223%20L286.313013%2C223%20C285.586166%2C223%20285%2C222.413834%20285%2C221.686987%20C285%2C220.960141%20285.586166%2C220.373974%20286.313013%2C220.373974%20L304.812427%2C220.373974%20C305.539273%2C220.397421%20306.101993%2C220.983587%20306.101993%2C221.686987%20Z%20M304.812427%2C211.69871%20L286.313013%2C211.69871%20C285.586166%2C211.69871%20285%2C212.284877%20285%2C213.011723%20C285%2C213.73857%20285.586166%2C214.324736%20286.313013%2C214.324736%20L304.812427%2C214.324736%20C305.539273%2C214.324736%20306.12544%2C213.73857%20306.12544%2C213.011723%20C306.101993%2C212.284877%20305.539273%2C211.69871%20304.812427%2C211.69871%20Z%20M286.313013%2C205.626026%20L304.812427%2C205.626026%20C305.539273%2C205.626026%20306.12544%2C205.039859%20306.12544%2C204.313013%20C306.12544%2C203.586166%20305.539273%2C203%20304.812427%2C203%20L286.313013%2C203%20C285.586166%2C203%20285%2C203.586166%20285%2C204.313013%20C285%2C205.039859%20285.586166%2C205.626026%20286.313013%2C205.626026%20Z%22%20id%3D%22icon-category%22%3E%3C/path%3E%0A%20%20%20%20%20%20%20%20%3C/g%3E%0A%20%20%20%20%3C/g%3E%0A%3C/svg%3E);
        background-repeat: no-repeat;
    }
    a:-webkit-any-link {
        color: -webkit-link;
        cursor: pointer;
        text-decoration: underline;
    }
    a {
        color: #293948;
        text-decoration: none;
        background-color: transparent;
    }
    .site-content {
        /* -moz-flex-grow: 1; */
        flex-grow: 1;
        height: 100%;
        height:100%;
        background-image: linear-gradient(rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0.5)),url(../assets/Relaxing_Full_HD_Film_Ocean_Live_Wallpaper_Dreamscene.gif);
        background-size: 100% auto;
    }
    p {
        font-family:'Quicksand','Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
        font-style: oblique;
        font-stretch: expanded;
        color:black;
        font-weight: bolder;
    }

  /* h3 {
    margin: 60px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  /* li {
    display: inline-block;
    margin: 0 10px;
  } */
  /* a {
    color: #c1ec24;
  } */
  </style>
  