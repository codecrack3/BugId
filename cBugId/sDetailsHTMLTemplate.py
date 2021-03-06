sDetailsHTMLTemplate = ("""
<!doctype html>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <style>
      * {
        border: 0;
        margin: 0;
        padding: 0;
        border-spacing: 0;
        border-collapse: collapse;
        color: rgba(22, 19, 16, 1);
        background: transparent;
        word-wrap: break-word;
        overflow-wrap: break-word;
        font-size: inherit;
      }
      html {
        background: #E5E2DE;
        font-weight: 400;
        padding: 1em;
        font-family: monospace;
      }
      body {
        margin: auto;
        max-width: 80em;
      }
      h1, h2, h3, h4, h5 {
        font-weight: 700;
      }
      a {
        color: inherit;
        text-decoration: none;
        margin-bottom: -1px;
      }
      :link {
        border-bottom: 1px dotted rgba(0,0, 238, 0.25);
      }
      :link:hover, :link:active {
        border-bottom: 1px solid rgba(0,0, 238, 1);
      }
      :visited {
        border-bottom: 1px dotted rgba(85, 26, 139, 0.25);
      }
      :visited:hover, :visited:active {
        border-bottom: 1px solid rgba(85, 26, 139, 1);
      }
      table {
        border-spacing: 0;
        border-collapse: collapse;
      }
      ul {
        padding-left: 2em;
      }
      h1 {
        padding: 0.5em 1em 0.5em 1em;
        color: rgba(255, 251, 247, 1);
        background-color: rgba(22, 19, 16, 1);
        font-size: 120%%;
        margin-bottom: 0.5em;
      }
      h2 {
        font-size: 120%%;
      }
      .Block {
        padding: 1em;
        border: 1px solid rgba(22, 19, 16, 0.2);
        border-radius: 0.5em;
        background-color: rgba(255, 251, 247, 1);
        box-shadow: 0 1em 2em rgba(22, 19, 16, 0.2), 0 1em 1em rgba(22, 19, 16, 0.05), 0 1em 0.5em rgba(22, 19, 16, 0.05);
        margin-bottom: 1em;
        display: block;
      }
      .Footer {
        padding: 1em;
        text-align: center;
      }
      .Important {
        background-color: rgba(255,255,0,0.3);
      }
      .SecurityImpact {
        background-color: rgba(255,0,0,0.2);
      }
      .CDBPrompt {
        white-space: pre;
      }
      .CDBCommand {
        font-weight: bold;
        white-space: pre;
      }
      .CDBStdOut {
        color: grey;
        white-space: pre;
      }
      .CDBOrApplicationStdOut {
        color: black;
        white-space: pre;
      }
      .CDBStdErr {
        color: maroon;
        white-space: pre;
      }
      .CDBIgnoredException {
        color: grey;
        white-space: pre;
      }
      .Stack {
        white-space: pre;
      }
      .StackIgnored {
        color: silver;
        white-space: pre;
      }
      .StackHash {
        font-weight: bold;
        background: rgba(255,255,0,0.2);
        white-space: pre;
      }
      .StackNoSymbol {
        font-style: italic;
        white-space: pre;
      }
      .StackSource {
        color: grey;
        white-space: pre;
      }
      .Registers {
        white-space: pre;
      }
      .Memory {
        white-space: pre;
      }
      .BinaryInformation {
        white-space: pre;
      }
      .DisassemblyInformation {
        white-space: pre;
      }
      .DisassemblyAddress {
        color: grey;
        white-space: pre;
      }
      .DisassemblyOpcode {
        color: grey;
        white-space: pre;
      }
      .DisassemblyInstruction {
        white-space: pre;
      }
      hr {
        border: dotted black;
        border-width: 0 0 1pt 0;
      }
    </style>
    <title>%(sId)s</title>
  </head>
  <body>
    <div class="Block">
      <h1>BugId v%(sBugIdVersion)s crash report</h1>
      <div class="Content">
        <table>
          <tr><td>BugId:                  &nbsp;</td><td><span class="Important">%(sId)s</span></td></tr>
          <tr><td>Description:            &nbsp;</td><td><span class="Important">%(sBugDescription)s</span></td></tr>
          <tr><td>Location:               &nbsp;</td><td><span class="Important">%(sBugLocation)s</span></td></tr>
          <tr><td>Security&nbsp;impact:   &nbsp;</td><td>%(sSecurityImpact)s</td></tr>
        </table>
        <br/>
        You may not use this version of BugId for commercial purposes.
        Please contact the author if you wish to use BugId commercially.
        Contact and licensing information can be found at the bottom of this report.
      </div>
    </div>
%(sBlocks)s
    <div class="Footer Block">
      <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">
        <img alt="Creative Commons License" style="vertical-align: middle; float: left;" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png"/>
      </a>
      This report was generated using <a href="https://github.com/SkyLined/BugId">BugId v%(sBugIdVersion)s</a>
        by <a href="mailto:berendjanwever@gmail.com">SkyLined</a>.<br/>
      BugId is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">
        Creative Commons Attribution-NonCommercial 4.0 International License</a>.<br/>
      Please contact the author if you wish to use BugId commercially.
    </div>
  </body>
</html>
""").strip("\r\n");
