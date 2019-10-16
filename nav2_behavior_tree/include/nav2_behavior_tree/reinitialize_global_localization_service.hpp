// Copyright (c) 2019 Samsung Research America
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#ifndef NAV2_BEHAVIOR_TREE__REINITIALIZE_GLOBAL_LOCALIZATION_SERVICE_HPP_
#define NAV2_BEHAVIOR_TREE__REINITIALIZE_GLOBAL_LOCALIZATION_SERVICE_HPP_

#include <string>
#include <memory>
#include <cmath>

#include "nav2_behavior_tree/bt_service_node.hpp"
#include "std_srvs/srv/empty.hpp"

namespace nav2_behavior_tree
{

class ReinitializeGlobalLocalizationService : public BtServiceNode<std_srvs::srv::Empty>
{
public:
  explicit ReinitializeGlobalLocalizationService(
    const std::string & service_node_name,
    const BT::NodeParameters & params)
  : BtServiceNode<std_srvs::srv::Empty>(service_node_name, params)
  {
    // default should be reinitialize_global_localization
    getParam<std::string>("service_name", service_name_);
  }

  void on_init() override
  {
  }
};

}  // namespace nav2_behavior_tree

#endif  // NAV2_BEHAVIOR_TREE__REINITIALIZE_GLOBAL_LOCALIZATION_SERVICE_HPP_
