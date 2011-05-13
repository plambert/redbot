"""\
<!DOCTYPE html>
<html>
<head>
	<title>REDbot: &lt;%(html_uri)s&gt;</title>
	<meta http-equiv="content-type" content="text/html; charset=utf-8" />
	<meta name="ROBOTS" content="INDEX, NOFOLLOW" />
    <link rel="stylesheet" type="text/css" href="%(static)s/style.css">
	<!--[if IE]> 
    <style type="text/css">
        #right_column {
        	width: 650px;
            float: left;
    </style>
    <![endif]-->
    <script type="text/javascript">
        var redbot_uri = "%(js_uri)s";
        var redbot_req_hdrs = [%(js_req_hdrs)s];
        var redbot_version = "%(version)s";
        function loadJS() {
            var element = document.createElement("script");
            element.src = "%(static)s/script.js";
            document.body.appendChild(element);
        }
        if (window.addEventListener)
            window.addEventListener("load", loadJS, false);
        else if (window.attachEvent)
            window.attachEvent("onload", loadJS);
        else
            window.onload = loadJS;
    </script>
    <!--script src="%(static)s/script.js" type="text/javascript"></script -->
    %(extra_js)s
</head>

<body>

<div id="popup"></div>
<form method="POST" id="save_form"
 action="?id=%(test_id)s&save=True%(descend)s">
</form>

<div id="request">
    <h1><a href="?"><span class="hilight"><abbr title="Resource Expert Droid">RED</abbr></span>bot</a>%(extra_title)s</h1>

    <form method="GET" onLoad="init_req_hdrs();" id="request_form">
        <input type="url" name="uri" value="%(html_uri)s" id="uri"/><br />
        <div id="req_hdrs"></div>
        <div class="add_req_hdr">
            <a href="#" id="add_req_hdr">add a request header</a>
        </div>
    </form>
</div>
"""