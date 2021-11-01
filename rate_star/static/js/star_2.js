//별점 마킹 모듈 프로토타입으로 생성
function Rating(){};
Rating.prototype.rate = 0;
Rating.prototype.setRate = function(newrate){
    //별점 마킹 - 클릭한 별 이하 모든 별 체크 처리
    this.rate = newrate;
    let items = document.querySelectorAll('.rate_radio');
    items.forEach(function(item, idx){
        if(idx < newrate){
            item.checked = true;
        }else{
            item.checked = false
        }
    });
}

let rating = new Rating();//별점 인스턴스 생성


document.addEventListener('DOMContentLoaded', function(){
   //별점선택 이벤트 리스너
    document.querySelector('.rating').addEventListener('click',function(e){
        let elem = e.target;
        console.log(elem)
        if(elem.classList.contains('rate_radio')){
            rating.setRate(parseInt(elem.value));
        }
    });
});


function counting() {
    let count = 0;
    var counting_obj = document.querySelectorAll('.rate_radio');
//    var counting_obj = document.getElementsByName("rating");
    var counting_leng = counting_obj.length;
    var checked = 0;
    for (i=0; i < counting_leng; i++) {
        if (counting_obj[i].checked == true) {
            checked += 1;
//            count++;
        }
    }
    console.log("checked " ,checked);
//    console.log(count);
    if (checked < 0 ) {
        alert("항목을 선택해주세요");
        return;
    }


    location.href="user/savestar/?checked="+checked;
}



