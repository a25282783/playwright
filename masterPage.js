// 此檔案內的程式碼會於各網站頁面載入
// add to wix velo

import wixLocation from 'wix-location';
import wixData from 'wix-data';

$w.onReady(function () {
    $w("#html,#html1,#html2").onMessage((event)=>{
      
        if(event.data.type === 'ready'){
          // do nothing yet, this is where the iframe is fully loaded
        }
        
        if(event.data.type === 'click'){
          // If clicked inside the html iframe execute this
          console.log(event.data.value);
          console.log("lets navigate to the other page now");
          wixLocation.to(event.data.value);
        }
      });	
});
