    /*
     * Licensed to the Apache Software Foundation (ASF) under one or more
     * contributor license agreements.  See the NOTICE file distributed with
     * this work for additional information regarding copyright ownership.
     * The ASF licenses this file to You under the Apache License, Version 2.0
     * (the "License"); you may not use this file except in compliance with
     * the License.  You may obtain a copy of the License at
     *
     *     http://www.apache.org/licenses/LICENSE-2.0
     *
     * Unless required by applicable law or agreed to in writing, software
     * distributed under the License is distributed on an "AS IS" BASIS,
     * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     * See the License for the specific language governing permissions and
     * limitations under the License.
     */
/**
 * Autogenerated by Thrift Compiler (0.9.1)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
package org.apache.airavata.model.appcatalog;


import java.util.Map;
import java.util.HashMap;
import org.apache.thrift.TEnum;

/**
 * Enumeration of Airavata supported Job Submission Mechanisms for High Perforamance Computing Clusters.
 * 
 * SSH:
 *  Execute remote job submission commands using via secure shell protocol.
 * 
 * GRAM:
 *  Execute remote jobs via Globus GRAM service.
 * 
 * UNICORE:
 *  Execute remote jobs via Unicore services
 * 
 */
@SuppressWarnings("all") public enum JobSubmissionProtocol implements org.apache.thrift.TEnum {
  SSH(0),
  GSISSH(1),
  GRAM(2),
  UNICORE(3);

  private final int value;

  private JobSubmissionProtocol(int value) {
    this.value = value;
  }

  /**
   * Get the integer value of this enum value, as defined in the Thrift IDL.
   */
  public int getValue() {
    return value;
  }

  /**
   * Find a the enum type by its integer value, as defined in the Thrift IDL.
   * @return null if the value is not found.
   */
  public static JobSubmissionProtocol findByValue(int value) { 
    switch (value) {
      case 0:
        return SSH;
      case 1:
        return GSISSH;
      case 2:
        return GRAM;
      case 3:
        return UNICORE;
      default:
        return null;
    }
  }
}
