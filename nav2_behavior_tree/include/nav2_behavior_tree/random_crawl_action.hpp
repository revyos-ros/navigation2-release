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

#ifndef NAV2_BEHAVIOR_TREE__RANDOM_CRAWL_ACTION_HPP_
#define NAV2_BEHAVIOR_TREE__RANDOM_CRAWL_ACTION_HPP_

#include <string>

#include "nav2_behavior_tree/bt_action_node.hpp"
#include "nav2_msgs/action/random_crawl.hpp"

namespace nav2_behavior_tree
{

class RandomCrawlAction : public BtActionNode<nav2_msgs::action::RandomCrawl>
{
public:
  explicit RandomCrawlAction(const std::string & action_name)
  : BtActionNode<nav2_msgs::action::RandomCrawl>(action_name)
  {
  }
};

}  // namespace nav2_behavior_tree

#endif  // NAV2_BEHAVIOR_TREE__RANDOM_CRAWL_ACTION_HPP_
