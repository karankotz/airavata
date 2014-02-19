/*
 *
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 *
*/
package org.apache.airavata.job.monitor.impl.push.amqp;

import org.apache.airavata.job.monitor.MonitorID;
import org.apache.airavata.job.monitor.core.PushMonitor;
import org.apache.airavata.job.monitor.exception.AiravataMonitorException;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * This is the implementation for AMQP based monitor, this uses
 * rabbitmq client to recieve AMQP based monitoring data from
 * mostly excede resources.
 */
public class AMQPMonitor extends PushMonitor {
    private final static Logger logger = LoggerFactory.getLogger(AMQPMonitor.class);

    @Override
    public boolean registerListener(MonitorID monitorID) throws AiravataMonitorException{
        return false;  //To change body of implemented methods use File | Settings | File Templates.
    }

    @Override
    public boolean unRegisterListener(MonitorID monitorID) throws AiravataMonitorException{
        return false;  //To change body of implemented methods use File | Settings | File Templates.
    }
}
