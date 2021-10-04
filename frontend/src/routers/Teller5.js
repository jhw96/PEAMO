import { useEffect } from 'react';
import './Teller5.css';
import { Link } from 'react-router-dom';

function Teller5() {
  // header 검은색으로 변경
  useEffect(() => {
    const header = document.querySelector('header');
    header.style.backgroundColor = '#1C1C1C';
  }, []);
  // header 검은색으로 변경

  return (
    <div className="teller5">
      <div className="teller_5">
        <div className="teller_question_5">
          <h2>향수를 뿌리고 싶은 계절은 언제인가요?</h2>
        </div>
        <div className="teller_image_5">
          <div className="image">
            <Link to="/teller-6">
              <img src="/images/spring.png" alt="spring"></img>
            </Link>
            <br></br>
            <Link to="/teller-6">
              <span>봄</span>
            </Link>
          </div>
          <div className="image">
            <Link to="/teller-6">
              <img src="/images/summer.png" alt="summer"></img>
            </Link>
            <br></br>
            <Link to="/teller-6">
              <span>여름</span>
            </Link>
          </div>
          <div className="image">
            <Link to="/teller-6">
              <img src="/images/fall.png" alt="fall"></img>
            </Link>
            <br></br>
            <Link to="/teller-6">
              <span>가을</span>
            </Link>
          </div>
          <div className="image">
            <Link to="/teller-6">
              <img src="/images/winter.png" alt="winter"></img>
            </Link>
            <br></br>
            <Link to="/teller-6">
              <span>겨울</span>
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Teller5;
