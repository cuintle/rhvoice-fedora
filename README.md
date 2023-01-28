<h1 align="center">RHVoice</h1>
<br>
<br>
<p align="center"><b>RHVoice</b> is a free and open source speech synthesizer by Olga Yakovleva</p>
<br/>

This repository exists to host specfiles, scripts and extra dictionaries used to build an updated version of **RHVoice** on COPR for **Fedora Linux** distribution.
 
https://copr.fedorainfracloud.org/coprs/cuintle/RHVoice  

### Added `talktext.sh` script

I know, its a terrible name. For now, supports only pt_BR and en_US, soon will get a `--language lang` param with all RHVoice supported languages. 

```Usage: talktext.sh [OPTIONS]
Speak copied or selected text using RHVoice

Defaults to pt_BR on Wayland.

  --pt                     Speak copied/selected text using portuguese voice
      --selection          Speaks selected text (works only on x11 sessions)
  --en                     Speak copied/selected text using english voice
      --selection          Speaks selected text (works only on x11 sessions)

  --help                   display this help and exit

Examples:
  talktext.sh --pt
  talktext.sh --en --selection
```

 ### Added extra dictionaries
Extra dictionaries from Big Linux.  
https://github.com/biglinux/rhvoice-brazilian-portuguese-complementary-dict-biglinux  

## License  

This project is licensed under the terms of the MIT license.
