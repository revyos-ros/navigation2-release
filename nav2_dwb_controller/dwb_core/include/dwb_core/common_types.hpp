// Copyright (c) 2018 Intel Corporation
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

#ifndef DWB_CORE__COMMON_TYPES_HPP_
#define DWB_CORE__COMMON_TYPES_HPP_

#include <memory>
#include "nav2_costmap_2d/costmap_2d_ros.hpp"
#include "tf2_ros/transform_listener.h"


namespace dwb_core
{

typedef std::shared_ptr<tf2_ros::Buffer> TFBufferPtr;
typedef std::shared_ptr<nav2_costmap_2d::Costmap2DROS> CostmapROSPtr;

}

#endif  // DWB_CORE__COMMON_TYPES_HPP_
