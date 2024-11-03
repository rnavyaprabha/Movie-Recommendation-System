import React, {useState} from 'react';
import Tabs from "./Tabs"
import {tabLabels} from "./constant"
const TabComponent = () => {
  const [activeTab, setActiveTab] = useState(tabLabels.WATCH_WHAT_YOU_LOVE);
  const onClickTab = (tab) => {
    setActiveTab(tab);
  }
    return (
    <div>
        <Tabs activeTabName={activeTab} onClickTab={onClickTab}/>
    </div>
  )
}

export default TabComponent;