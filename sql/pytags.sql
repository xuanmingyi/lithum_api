/*
 Navicat Premium Data Transfer

 Source Server         : 172.16.29.32
 Source Server Type    : MySQL
 Source Server Version : 50556
 Source Host           : localhost:3306
 Source Schema         : zabbix

 Target Server Type    : MySQL
 Target Server Version : 50556
 File Encoding         : 65001

 Date: 05/09/2018 14:11:54
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for pytags
-- ----------------------------
DROP TABLE IF EXISTS `pytags`;
CREATE TABLE `pytags`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tag_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `color` varchar(7) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_at` timestamp NULL DEFAULT NULL,
  `update_at` timestamp NULL DEFAULT NULL,
  `delete_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 47 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of pytags
-- ----------------------------
INSERT INTO `pytags` VALUES (41, 'tag-ibs3ouqq', '物理机', '#562339', '2018-09-04 15:29:20', '2018-09-04 15:47:23', NULL);
INSERT INTO `pytags` VALUES (42, 'tag-ivkp8n0e', '测试一下', '#345623', '2018-09-04 17:25:10', NULL, NULL);
INSERT INTO `pytags` VALUES (43, 'tag-y5e8yt25', '测试一下', '#345623', '2018-09-04 17:25:11', NULL, NULL);
INSERT INTO `pytags` VALUES (44, 'tag-wzbipq0q', '测试一下', '#345623', '2018-09-04 17:25:19', NULL, NULL);
INSERT INTO `pytags` VALUES (45, 'tag-fxwy6k4n', '测试一下', '#345623', '2018-09-04 17:25:19', NULL, NULL);
INSERT INTO `pytags` VALUES (46, 'tag-mt5j60ow', '测试一下', '#345623', '2018-09-04 17:25:20', NULL, NULL);

SET FOREIGN_KEY_CHECKS = 1;
