import React from 'react';
import { tabLabels } from './constant';
import { Link } from 'react-router-dom';
import"./Tabs.css"

const Tabs = ({activeTabName, onClickTab}) => {
  const{WATCH_WHAT_YOU_LOVE, CHOOSE_FROM_1000S, FOR_FREE} = tabLabels;

  const renderTabTitle =(tabTitle, isActive, icon, id) => (
    <div 
        onClick={() => onClickTab(tabTitle)} 
        id={id} 
        className={`tab-item ${isActive && "tab-border" }`}
    >
        <i className={icon}></i>
        <p>{tabTitle}</p>

    </div>
  )
    return (
    <>
        <section className='tabs'> 
            <div className='container'>
                {renderTabTitle(
                    WATCH_WHAT_YOU_LOVE, 
                    activeTabName === WATCH_WHAT_YOU_LOVE, 
                    "fa-solid fa-film fa-3x", 
                    "tab-1"
                    )}
                {renderTabTitle(
                    CHOOSE_FROM_1000S, 
                    activeTabName === CHOOSE_FROM_1000S, 
                    "fa-solid fa-video fa-3x", 
                    "tab-2"
                    )}
                {renderTabTitle(
                    FOR_FREE, 
                    activeTabName === FOR_FREE, 
                    "fa-solid fa-ticket fa-3x", 
                    "tab-3"
                    )}

            </div>
        </section>
        {activeTabName === WATCH_WHAT_YOU_LOVE && (
            <section className="tab-content">
                <div className='container'>
                    <div id="tab-1-content" className={`tab-content-item ${activeTabName === WATCH_WHAT_YOU_LOVE && "show"}`}>
                        <div className='tab-1-content-inner'>
                            <div>
                                <p className='text-ig'>
                                    Personalized suggestions — discovered through the things you already love!
                                </p>
                                <Link to="/homepage" className='btn btn-lg'>
                                    Ready to Binge
                                </Link>
                            </div>
                            <img src='https://images5.alphacoders.com/445/445155.jpg' alt=''/>
                        </div>
                    </div>
                </div>
            </section>
        )}
        {activeTabName === CHOOSE_FROM_1000S && (
            <section className='tab-content'>
                <div className='container'>
                    <div id="tab-2-content" className={`tab-content-item ${activeTabName === CHOOSE_FROM_1000S && "show"}`}> 
                        <div className='tab-2-content-tap'>
                            <p className='text-ig'>
                                Find Movies right from old classics to newest blockbuster to fit your mood and choices.
                            </p>
                            <Link to='/homepage' className='btn btn-lg'>
                                Ready to Binge
                            </Link>
                        </div>
                        <div className='tab-2-content-bottom'>
                            <div>
                                <img src='https://www.rd.com/wp-content/uploads/2023/03/mystery-movies-opener-3.2.gif?fit=700%2C467' alt=''/>
                                <p className='text-md'>Dwell in any emotion.</p>
                                <p className='text-dark'>
                                    Tearfull sadness or absolute anger driven horror? We got you covered with the very best movies recommendations for any mood or feeling.
                                </p>
                            </div>
                            <div>
                                <img src='https://www.mesaonline.org/wp-content/uploads/2022/08/gracenote_id_distribution_system_PR1.jpg' alt='' />
                                <p className='text-md'>
                                    Trusted recommendations.
                                </p>
                                <p className='text-dark'>
                                    We take you experience very SERIOUSLY!
                                </p>
                            </div>
                            <div>
                                <img src='https://www.plex.tv/wp-content/uploads/2024/01/Watch-Free-Hero-2048x1152-3.png' alt='' />
                                <p className='text-md'>
                                    We are one of the Best.
                                </p>
                                <p className='text-dark'>
                                    Trust us, We have watched atleast 60% of the movies our site recommends!
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        )}
        {activeTabName === FOR_FREE && (
            <section className='tab-content'>
                <div className='container'>
                    <div id="tab-3-content" className={`tab-content-item ${activeTabName === FOR_FREE && "show"}`}> 
                        <div className='text-center'>
                            <p className='text-lg'>
                                Guess What? 
                                It's free of cost 
                            </p>
                            <Link to='/homepage' className='btn btn-lg'>Ready to Binge</Link>
                        </div>
                        <div>
                            <img src='https://cdn.vox-cdn.com/thumbor/-_58CyCjSLS36byYJ3jyjvy4Akg=/1400x1050/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/9871033/Movies_end_of_year_2017.jpg' alt=''/>
                        </div>
                    </div>
                </div>
            </section>
        )}
    </>
  )
}

export default Tabs